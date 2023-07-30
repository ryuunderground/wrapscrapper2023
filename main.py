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
        job_names = soup.find_all('a', class_="title dev_view"))
        job_search = False
