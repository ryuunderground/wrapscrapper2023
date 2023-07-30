from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests

"""base_url = "https://www.jobkorea.co.kr/Search/?stext="
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
"""


def say_hello(name, age):
    print(f"Hello {name}. U are {age} years old")


say_hello("Ryu", 25)
say_hello(age=25, name="Ryu")
