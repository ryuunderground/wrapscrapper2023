from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests

base_url = "https://www.jobkorea.co.kr/Search/?stext="
search_term = "인턴"
response = requests.get(f"{base_url}{search_term}")
"""
job_search = True
while job_search:
    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        job_posts = soup.find_all('li', class_="list-post")
        for post in job_posts:
            post_list_info = post.find_all('div', class_="post-list-info")
            for pli in post_list_info:
                # pli.pop(-1)
                # ^마지막 요소 제거
                for anchors in pli.find_all('a'):
                    anchor = anchors.get('href')
                    if not anchor.endswith('logpath=1') and not anchor.endswith('g7intern'):
                        links = []
                        links.append(anchor)
                        print(links)
        job_search = False"""

list_prac = [1, 2, 3]
first, second, third = list_prac
print(first, second, third)
# 결과
# 1 2 3
