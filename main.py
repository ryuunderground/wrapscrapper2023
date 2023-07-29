websites = (
    "https://google.com",
    "https://instagram.com",
    "https://youtube.com",
    "airbnb.com",
    "pornhub.com",
    "https://naver.com"
)

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website)
