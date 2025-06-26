VNFD_PATH = "../VFND-vietnamese-fake-news-datasets/Dataset"
VNFD_SEARCH = "vfnd_new_google_search.xlsx"

CX = "9142078c1c2ee4c76"

APIs = [
    "AIzaSyDI7dBRyyImKbw8tuCKc6VKlJmPpPGkuN0", # hgvanything
    "AIzaSyDbXD3IISubT6iDtnuA2HIn65Rz6anZc1o", # LemNhem
    "AIzaSyBiVxbNSPDP1kBGd77t7_OzDsQzWiZVZrg", # vohoang22042204
    "AIzaSyBUtBNcSJ1-9HNIDhE7zPY1WuCgnB8Gr4A", # Quynh
    "AIzaSyAqoHbltwdao4qcWU1TZC7zuJaEXRXdj6k", # savoury
    "AIzaSyCP9QDM7hZtW4lqT3DdMuEyeVqcG3V1-TY", # voh631
]

# CX_API = [
#     ("9142078c1c2ee4c76", "AIzaSyDI7dBRyyImKbw8tuCKc6VKlJmPpPGkuN0"), # hgvanything
#     ("91071eeac4f6b4ba5", "AIzaSyDbXD3IISubT6iDtnuA2HIn65Rz6anZc1o"), # LemNhem
#     ("4207133612371473a", "AIzaSyBiVxbNSPDP1kBGd77t7_OzDsQzWiZVZrg"), # vohoang22042204
# ]


# Selenium Configuration
CHROME_DRIVER_VERSION = 133  # Update this as needed
HEADLESS = True
MAX_PROCESSES = 1  # Max is 8
file_paths = [
    f"CrawlingNo{i}.xlsx" for i in range(1, 18)
]
RETRIES = 3


# Crawling Settings
START_URL = r"https://notebooklm.google.com?hl=en"

# Excel Configuration
EXCEL_FILE = fr"/Data/vfnd_new_google_search.xlsx"
ERROR_LOG_SHEET = "Error Log"

# Logging Configuration
LOG_FILE = "crawler.log"

TXT_DIRECTORIES = [fr"D:\Programming\Python\Web-Summarizer-with-NotebookLMs\Data\vnfd_search_txt\{i}" for i in
                   range(1, 275)] # 274 is the number of rows of EXCEL_FILE



# List of Vietnamese news websites for crawling
websites = [
    "vnexpress.net",
    "tuoitre.vn",
    "thanhnien.vn",
    "vietnamplus.vn",
    "vietnamnet.vn"
]

# Google accounts
ACCOUNTS = [  # (Email, Password)
    ("vh22042204@gmail.com", "Helloworld@123"),
    ("lemnhem0610@gmail.com", "Lem_nhem_0610"),
    ("vhganything0001@gmail.com", "qwertyuiop@1234567890")
]

N_ACCOUNTS = len(ACCOUNTS)

# Prompts
PROMPTS_DICT = {
    "vi": "",
    "en": ""
}

# List of Vietnamese news websites for crawling
websites = [
    "vnexpress.net",
    "tuoitre.vn",
    "thanhnien.vn",
    "vietnamplus.vn",
    "vietnamnet.vn"
]


# Number of Prompts
NUMBER_OF_PROMPTS = len(PROMPTS_DICT)