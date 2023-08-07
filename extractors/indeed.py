from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 브라우저 꺼짐 방지 코드

browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
# 크롬드라이버를 최신으로 유지해줍니다

driver = webdriver.chrome()
base_url_head = "https://kr.indeed.com/jobs?q="
base_url_tail = "vjk=938c3c09748cc0cd"
search_keyword = "인턴"
location_keyword = "서울"
driver.get(
    f"{base_url_head}{search_keyword}={location_keyword}{base_url_tail}")

# print(driver.page_source)

if response.status_code != 200:
    print("Can't request website")
else:
    stack = 0
    soup = BeautifulSoup(response.text, "html.parser")
    job_posts = soup.find_all('li')
    print(len(job_posts))
