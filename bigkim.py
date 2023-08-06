from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests


base_url = "https://www.bigkim.org/논문/"
response = requests.get(base_url)
results = []
if response.status_code != 200:
    print("Can't request page.")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    publication_soup = soup.find_all(
        'div', class_="elementor-widget-container")
    for anchors in publication_soup:
        publications = anchors.find_all('a')
        for is_raw in publications:
            subjects_raw = is_raw.find_all('i')
            for pure_subjects in subjects_raw:
                subjects = pure_subjects.string
                if subjects == None:
                    print('-')
                else:
                    print(subjects)
        for titles_raw_raw in publications:
            titles_raw = titles_raw_raw.stripped_strings
            for pure_titles in titles_raw:
                titles = pure_titles
                # print(titles)
                # print("/////////////")
        for hrefs in publications:
            links = hrefs.get('href')
            data_dic = {
                'title': titles,
                'link': links
            }
            # print(data_dic)
