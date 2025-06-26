import logging
from crawler.config import LOG_FILE


def setup_logger():
    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Clear existing handlers to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    # Formatter for consistent log formatting
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # File handler (writes to a log file)
    file_handler = logging.FileHandler(LOG_FILE, mode='w', encoding='utf-8', delay=False)  # Disable buffering
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler (writes to the terminal)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)