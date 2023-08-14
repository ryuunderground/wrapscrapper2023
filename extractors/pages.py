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
base_url_tail = "&fromage=7&vjk=1b45b4877109169b"
search_keyword = "인턴"
location_keyword = "서울"
driver.get(
    f"{base_url_head}{search_keyword}&l={location_keyword}{base_url_tail}")


def get_last_page():
    soup = BeautifulSoup(driver.page_source, "html.parser")
    pagination = soup.find("a", {"data-testid": "pagination-page-next"})
    if pagination != None:
        go_to_next_page = pagination["href"]
        next_url = "https://kr.indeed.com"
        if not go_to_next_page.startswith("https://"):
            go_to_next_page = f"{next_url}{go_to_next_page}"
            print(go_to_next_page)
            driver.get(go_to_next_page)
            get_last_page()
    else:
        print("finally")
        """last_pagination = soup.find(
            "button", {"data-testid": "pagination-page-current"})
        print(last_pagination.text)"""


get_last_page()

while (True):
    pass
