from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests


base_url = "https://www.bigkim.org/논문/"
response = requests.get(base_url)
results = []
titles = []
links = []
if response.status_code != 200:
    print("Can't request page.")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    publication_soup = soup.find_all(
        'div', class_="elementor-widget-container")
    for anchors in publication_soup:
        publications = anchors.find_all('a')
        for hrefs in publications:
            httpss = hrefs.get('href')
            if httpss.startswith("https"):
                links.append(httpss)
        for titles_raw_raw in publications:
            titles_raw = titles_raw_raw.stripped_strings
            for pure_titles in titles_raw:
                names = pure_titles
                years = 2024
                while years >= 2018:
                    years = years - 1
                    if f"{years})" in names:
                        titles.append(names)
                        """data_dic = {
                            'title': titles,
                            'link': links
                        }"""
    print(len(links))
    print(len(titles))
    # print(data_dic)
