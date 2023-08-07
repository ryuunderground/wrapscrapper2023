from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests

base_url_head = "https://kr.indeed.com/jobs?q="
base_url_tail = "vjk=938c3c09748cc0cd"
search_keyword = "인턴"
location_keyword = "서울"
response = requests.get(
    f"{base_url_head}{search_keyword}={location_keyword}{base_url_tail}")

if response.status_code != 200:
    print("Can't request website")
else:
    stack = 0
    soup = BeautifulSoup(response.text, "html.parser")
    job_posts = soup.find_all('li')
    print(len(job_posts))
