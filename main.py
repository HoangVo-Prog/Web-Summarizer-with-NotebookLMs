import logging
import multiprocessing
import os

from crawler.config import TXT_FOLDERS, EXCEL_FILE, MAX_PROCESSES, ACCOUNTS, N_ACCOUNTS
from crawler.core import login_with_undetected_driver
from crawler.logger import setup_logger


def worker(args):
    worker_id, (folders_paths, excel_file), init_lock = args

    setup_logger()

    # Determine which account to use for this worker
    account_index = worker_id // N_ACCOUNTS
    email, password = ACCOUNTS[account_index]

    logging.info(f"Worker {worker_id} is waiting to initialize...")

    driver = None
    try:
        # Sequential Initialization
        with init_lock:  # Only one worker can initialize at a time
            logging.info(f"Worker {worker_id} is initializing...")
            driver, workbook, sheet, processed_indexes = login_with_undetected_driver(folders_paths,
                                                                                    excel_file,
                                                                                    email,
                                                                                    password,
                                                                                    initialize_only=True)
            logging.info(f"Worker {worker_id} finished initialization.")

        # Parallel Crawling
        logging.info(f"Worker {worker_id} is starting to crawl files...")
        login_with_undetected_driver(folders_paths,
                                     excel_file,
                                     email,
                                     password,
                                     driver=driver,
                                     initialize_only=False,
                                     workbook=workbook,
                                     sheet=sheet,
                                     processed_indexes=processed_indexes)

    except Exception as e:
        logging.error(f"Worker {worker_id} encountered an error: {e}", exc_info=True)
    finally:
        if driver:
            driver.quit()
            logging.info(f"Worker {worker_id}'s browser has been closed.")


def main():
    # Verify directories
    for d in os.listdir(TXT_FOLDERS):
        if not os.path.exists(d):
            pass
            # return
    # Pair up directories with Excel files
    tasks = [(TXT_FOLDERS, EXCEL_FILE)]
    indexed_tasks = list(enumerate(tasks))
    # Use a multiprocessing.Manager to create a shared lock
    with multiprocessing.Manager() as manager:
        init_lock = manager.Lock()

        # Pass the lock to each worker
        tasks_with_locks = [(worker_id, task, init_lock) for worker_id, task in indexed_tasks]

        # Start multiprocessing pool
        processes = min(MAX_PROCESSES, len(tasks))

        with multiprocessing.Pool(processes=processes) as pool:
            pool.map(worker, tasks_with_locks)

    logging.info("All crawling tasks completed.")


if __name__ == "__main__":
    main()
