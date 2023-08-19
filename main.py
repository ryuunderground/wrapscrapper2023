from flask import Flask, render_template, request
from extractors.indeed import indeed_job_extract
from extractors.jobkorea import extract_jobkorea_jobs

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="Ryu")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    location = request.args.get("location")
    indeed = indeed_job_extract(keyword, location)
    jobkorea = extract_jobkorea_jobs(keyword)
    jobs = indeed + jobkorea
    return render_template("search.html", keyword=keyword, location=location, jobs=jobs)


app.run("127.0.0.1")
