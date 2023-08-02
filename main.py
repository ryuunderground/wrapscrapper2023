from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests

base_url = "https://www.jobkorea.co.kr/Search/?stext="
search_term = "인턴"
response = requests.get(f"{base_url}{search_term}")

job_search = True
while job_search:
    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        job_posts = soup.find_all('li', class_="list-post")
        for post in job_posts:
            """회사 이름 따오기
            post_list_corp = post.find_all(
                'div', class_="post-list-corp")
            for plc in post_list_corp:
                for anchors in plc.find_all('a'):
                    company = anchors.get('title')
                    if company != "새창":
                        companies = []
                        companies.append(company)
                        print(companies)"""
            post_list_info = post.find_all('div', class_="post-list-info")
            for pli in post_list_info:
                for anchors in pli.find_all('a'):
                    anchor = anchors.get('href')
                    links = []
                    if not anchor.endswith('logpath=1') and not anchor.endswith('g7intern'):
                        links.append(anchor)
                    title = anchors.get('title')
                    if title != None:
                        titles = []
                        titles.append(title)
                for span in pli.find_all('span', class_="loc short"):
                    location = str(span)
                    locations = []
                    locations.append(location[24:-7])
                    print(titles, locations, links)
                    job_data = {'company': str(titles),
                                'region': str(locations),
                                'apply': str(links)}

        job_search = False
