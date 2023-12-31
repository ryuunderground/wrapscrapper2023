from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests


def extract_jobkorea_jobs(keyword):
    base_url = "https://www.jobkorea.co.kr/Search/?stext="
    response = requests.get(f"{base_url}{keyword}")

    results = []
    job_search = True
    while job_search:
        if response.status_code != 200:
            print("Can't request website")
        else:
            stack = 0
            soup = BeautifulSoup(response.text, "html.parser")
            job_posts = soup.find_all('li', class_="list-post")
            for post in job_posts:
                post_list_corp = post.find_all(
                    'div', class_="post-list-corp")
                for plc in post_list_corp:
                    for anchors in plc.find_all('a'):
                        companies = anchors.get('title')
                post_list_info = post.find_all('div', class_="post-list-info")
                for pli in post_list_info:
                    for anchors in pli.find_all('a'):
                        anchor = anchors.get('href')
                        title_raw = anchors.get('title')
                        for span in pli.find_all('span', class_="loc short"):
                            if stack == 20:
                                break
                            else:
                                stack = stack + 1
                                company = companies
                                link = anchor
                                title = title_raw
                                location = span
                                job_data_dic = {
                                    'link': f"https://www.jobkorea.co.kr/{link}",
                                    'company': company.replace(",", " "),
                                    'location': location.string.replace(",", " "),
                                    'position': title.replace(",", " ")
                                }
                                results.append(job_data_dic)
            job_search = False
    return results
