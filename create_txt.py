from tqdm import tqdm
from crawler.utils import create_txt_file
from crawler.config import VNFD_SEARCH
import pandas as pd
import os
import ast


if __name__ == "__main__":
    vfnd_search = pd.read_excel(os.path.join(os.getcwd(), "Data", VNFD_SEARCH))
    os.makedirs("Data/vnfd_search_txt", exist_ok=True)
    for idx, row in tqdm(vfnd_search.iterrows(), total=len(vfnd_search)):
        results = row["google_search"] if row["google_search"] else []
        if len(results) == 0:
            pass
        results = ast.literal_eval(results)
        print(results)
        print(type(results[0]))
        # for i, url in enumerate(results):
        #     stop = True
        #     os.makedirs(f"Data/vnfd_search_txt/{idx+1}", exist_ok=True)
        #     create_txt_file(url, f"Data/vnfd_search_txt/{idx+1}/{idx+1}_{i}.txt")
