from bs4 import BeautifulSoup
# pip install bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(search_keyword, location_keyword):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
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
    soup = BeautifulSoup(driver.page_source, "html.parser")
    pagination = soup.find("nav", {"aria-label": "pagination"})
    if pagination == None:
        return 1
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


def indeed_job_extract(search_keyword, location_keyword):
    pages = get_page_count(search_keyword, location_keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_experimental_option("detach", True)
        # 브라우저 꺼짐 방지 코드

        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=chrome_options)
        # 크롬드라이버를 최신으로 유지해줍니다
        base_url_head = "https://kr.indeed.com/jobs"
        final_url = f"{base_url_head}?q={search_keyword}&l={location_keyword}&fromage=7&start={page*10}&vjk=1b45b4877109169b"
        print("Requesting", final_url)
        driver.get(final_url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_posts = soup.find(
            'ul', class_="jobsearch-ResultsList")
        # recursive=False
        # 후손이 아닌 직계 자손만 검색
        for posts in job_posts:
            anchors = posts.select_one("h2 a")
            if anchors != None:
                titles = anchors['aria-label']
                links = anchors['href']
            # for anchors in posts.find_all('a', class_="jcs-JobTitle css-jspxzf eu4oa1w0"):
            #    titles = anchors.get('aria-label')
            #    links = anchors.get('href')
            #    print(links)
            names = posts.find("span", class_="companyName")
            if names != None:
                nms = names
            locations = posts.find("div", class_="companyLocation")
            if locations != None:
                locs = locations
            job_datas = {
                'link': f"https://kr.indeed.com/{links}",
                'company': nms.string.replace(",", " "),
                'location': locs.string.replace(",", " "),
                'position': titles.replace(",", " ")
            }
            results.append(job_datas)
    return results


while (True):
    pass
