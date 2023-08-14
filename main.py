from extractors.jobkorea import extract_jobkorea_jobs
from extractors.indeed import indeed_job_extract

keyword, location = input("what are you looking for?").split()
print(f"{keyword}and{location}")
"""indeed = indeed_job_extract(keyword, location)
jobkorea = extract_jobkorea_jobs(keyword)

jobs = indeed + jobkorea
for job in jobs:
    print(job)
    print("///////////\n//////")"""
