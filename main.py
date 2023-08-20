from flask import Flask, render_template, request, redirect
from extractors.indeed import indeed_job_extract
from extractors.jobkorea import extract_jobkorea_jobs

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="Ryu")


db = {}


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    location = request.args.get("location")
    if keyword == None or location == None or keyword == "" or location == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = indeed_job_extract(keyword, location)
        jobkorea = extract_jobkorea_jobs(keyword)
        jobs = indeed + jobkorea
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, location=location, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    location = request.args.get("location")
    if keyword == None or location == None or keyword == "" or location == "":
        return redirect("/")
    if keyword not in db or location not in db:
        return redirect(f"/search?keyword={keyword}&location={location}")


app.run("127.0.0.1")
