from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests
from extractors.jobkorea import extract_jobkorea_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-snadbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.chrome(options=Options)

jobs = extract_jobkorea_jobs("인턴")
print(jobs)
