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
        stack = 0
        results = []
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
                    title_raw = anchors.get('title')
                    if stack == 20:
                        break
                    else:
                        stack = stack + 1
                        link = anchor
                        title = title_raw
                    for span in pli.find_all('span', class_="loc short"):
                        location_raw = str(span)
                        location = location_raw[24:-7]
                job_data_dic = {'company': title,
                                'region': location,
                                'apply': link}
                results.append(job_data_dic)
            print(results)
            job_search = False
