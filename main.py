from extractors.indeed import indeed_job_extract
from extractors.jobkorea import extract_jobkorea_jobs

search_keyword, location_keyword = input("what are you looking for?").split()
print(f"{search_keyword}and{location_keyword}")

indeed = indeed_job_extract(search_keyword, location_keyword)
jobkorea = extract_jobkorea_jobs(search_keyword)

jobs = indeed + jobkorea

jobs = jobkorea

file = open(f"{search_keyword}.csv", "w", encoding="utf-8-sig")
file.write("Position,Company,Location,Url\n")

for job in jobs:
    file.write(
        f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()

while (True):
    pass
