import requests
res = requests.get("https://naver.com")
print("응답코드 : ", res.status_code)
