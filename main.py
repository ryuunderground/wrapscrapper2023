from bs4 import BeautifulSoup
# pip install bs4
import requests
# pip install requests
from extractors.jobkorea import extract_jobkorea_jobs

jobs = extract_jobkorea_jobs("인턴")
print(jobs)
