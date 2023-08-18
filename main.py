from extractors.jobkorea import extract_jobkorea_jobs
from extractors.indeed import indeed_job_extract
from file import save_to_file

search_keyword, location_keyword = input("what are you looking for?").split()
print(f"{search_keyword}and{location_keyword}")

indeed = indeed_job_extract(search_keyword, location_keyword)
jobkorea = extract_jobkorea_jobs(search_keyword)

jobs = indeed + jobkorea

save_to_file(search_keyword, jobs)

"""form flask import Flask
app = Flask("JobScrapper)
@app.route("/")
def home():
return "hey there!"

app.run("127.0.0.1")"""
