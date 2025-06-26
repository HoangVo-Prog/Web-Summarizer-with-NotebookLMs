import os
from tqdm import tqdm
import requests
import urllib.parse
from crawler.config import APIs, CX
import pandas as pd
from crawler.exceptions import OutOfQuotaException
import time


def is_api_key_available(api_key):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': 'test',  # Fake search engine ID
        'q': 'test'  # Dummy query
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    try:
        response = requests.get(url)
        if response.status_code == 403 or 'dailyLimitExceeded' in response.text:
            return False
        return True
    except:
        return False


def check_available_apis(APIs):
    available_apis = []
    for api in APIs:
        if is_api_key_available(api):
            available_apis.append(api)
    return available_apis


def replace_API_KEY(APIs, index):
    if index > len(APIs):
        raise Exception("No more API keys available")
    return APIs[index]


def search_google(query, num_results=3):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": query,
        "num": num_results  # số kết quả (tối đa 10/lần gọi)
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        results = response.json().get("items", [])
        return [{"displayLink": item.get("displayLink"),
                 "link": item.get("link")
                } for item in results]

        # return [item.get("link") for item in results]
    else:
        print("❌ Lỗi khi gọi API:", response.status_code, API_KEY)
        raise OutOfQuotaException


if __name__ == "__main__":
    index = 0
    available_apis = check_available_apis(APIs)
    if not available_apis:
        print("No available API keys found")
        exit(1)

    API_KEY = available_apis[index]

    vfnd = pd.read_excel(os.path.join(os.getcwd(), "Data", "vfnd_new_normalize.xlsx"))
    google_search_results = []

    for idx, row in tqdm(vfnd.iterrows(), total=len(vfnd)):
        search_query = row['title'] if row['title'] else row['text']
        try:
            results = search_google(search_query)
            google_search_results.append(results)
        except OutOfQuotaException as e1:
            try:
                index += 1
                API_KEY = replace_API_KEY(APIs, index)
                print("Switching to API key:", API_KEY)
                results = search_google(search_query)
                google_search_results.append(results)
            except Exception as e2:
                print("An error occurs:", e2)
                google_search_results.append(None)

        time.sleep(2)

    vfnd['google_search'] = google_search_results
    output_path = os.path.join(os.getcwd(), "Data", "vfnd_new_normalize_google_search.xlsx")
    vfnd.to_excel(output_path, index=False)
    print("Done!")