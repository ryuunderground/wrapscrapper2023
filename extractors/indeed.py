from bs4 import BeautifulSoup
# pip install bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 브라우저 꺼짐 방지 코드

browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
# 크롬드라이버를 최신으로 유지해줍니다

driver = webdriver.Chrome()
base_url_head = "https://kr.indeed.com/jobs?q="
base_url_tail = "&vjk=938c3c09748cc0cd"
search_keyword = "인턴"
location_keyword = "서울"
browser.get(
    f"{base_url_head}{search_keyword}&l={location_keyword}{base_url_tail}")

print(browser.page_source)

"""if driver.status_code != 200:
    print("Can't request website")
else:
    stack = 0
    soup = BeautifulSoup(driver.text, "html.parser")
    job_posts = soup.find_all('li')
    print(len(job_posts))"""
while (True):
    pass
