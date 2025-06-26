VNFD_PATH = "../VFND-vietnamese-fake-news-datasets/Dataset"
VNFD_SEARCH = "vfnd_new_google_search.xlsx"

CX = ""

APIs = [
]

# CX_API = [
#     ("9142078c1c2ee4c76", "AIzaSyDI7dBRyyImKbw8tuCKc6VKlJmPpPGkuN0"), # hgvanything
#     ("91071eeac4f6b4ba5", "AIzaSyDbXD3IISubT6iDtnuA2HIn65Rz6anZc1o"), # LemNhem
#     ("4207133612371473a", "AIzaSyBiVxbNSPDP1kBGd77t7_OzDsQzWiZVZrg"), # vohoang22042204
# ]


# Selenium Configuration
CHROME_DRIVER_VERSION = 133  # Update this as needed
HEADLESS = False
MAX_PROCESSES = 1  # Max is 8
file_paths = [
    f"CrawlingNo{i}.xlsx" for i in range(1, 18)
]
RETRIES = 3


# Crawling Settings
START_URL = r"https://notebooklm.google.com?hl=en"

# Excel Configuration
EXCEL_FILE = fr"D:\Programming\Python\Web-Summarizer-with-NotebookLMs\Data\vfnd_new_normalize_notebookLMs.xlsx"
ERROR_LOG_SHEET = "Error Log"

# Logging Configuration
LOG_FILE = "../crawler.log"

TXT_FOLDERS = fr"D:\Programming\Python\Web-Summarizer-with-NotebookLMs\Data\vnfd_search_txt" # 274 is the number of rows of EXCEL_FILE



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
    ("abd@gmail.com", ""),
    ("abd0610@gmail.com", ""),
    ("jdfk@gmail.com", "")
]

N_ACCOUNTS = len(ACCOUNTS)

# Prompts
PROMPTS_DICT = {
    "vi":
        """Hãy đọc tất cả các file tôi đã cung cấp trong Notebook.  
Với mỗi file, hãy tóm tắt nội dung chính một cách ngắn gọn, rõ ràng và súc tích nhất.  
Định dạng bắt buộc như sau (giữ nguyên cấu trúc dòng và tab):
\"\"\"
<ten_file_1>
    <nội dung tóm tắt file 1>
<ten_file_2>
    <nội dung tóm tắt file 2>
...
\"\"\"
Không thêm bất kỳ nhận xét hoặc phần giải thích nào khác ngoài định dạng trên.  
Nếu một file không có nội dung đáng chú ý, chỉ cần ghi rõ là:
\"\"\"
<ten_file>
    Không có nội dung đáng chú ý.
\"\"\"
"""
,
    "en":
        """Please read all the files I have provided in the Notebook.  
For each file, summarize the main content concisely, clearly, and in a focused manner.  
The output format must strictly follow this structure (preserve exact lines and tab indentation):
\"\"\"
<file1_name>
    <summary of file 1>
<file2_name>
    <summary of file 2>
...
\"\"\"
Do not add any extra comments or explanations beyond this format.  
If a file contains no notable content, just write:
\"\"\"
<file_name>
    No notable content.
\"\"\"
"""
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