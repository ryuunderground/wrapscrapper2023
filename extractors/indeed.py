from bs4 import BeautifulSoup
# pip install bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 브라우저 꺼짐 방지 코드

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
# 크롬드라이버를 최신으로 유지해줍니다

base_url_head = "https://kr.indeed.com/jobs?q="
base_url_tail = "&vjk=938c3c09748cc0cd"
search_keyword = "인턴"
location_keyword = "서울"
driver.get(
    f"{base_url_head}{search_keyword}&l={location_keyword}{base_url_tail}")

soup = BeautifulSoup(driver.page_source, "html.parser")
job_posts = soup.find_all(
    'ul', class_="jobsearch-ResultsList css-0")
# recursive=False
# 한 사이클만 돌아감, 재귀 X
for posts in job_posts:
    for anchors in posts.find_all('a', class_="jcs-JobTitle css-jspxzf eu4oa1w0"):
        print(anchors)
        titles = anchors.get('aria-label')
        # print(titles)

while (True):
    pass
