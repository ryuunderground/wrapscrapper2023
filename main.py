import requests

websites = (
    "naver.com",
    "https://google.com",
    "https://daum.net",
    "https://instagram.com",
    "youtube.com"
)
results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = requests.get(website)
    if response.status_code == 200:
        results[website] = "OK"
    else:
        results[website] = "Failed"
print(results)
