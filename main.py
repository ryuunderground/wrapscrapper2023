from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import indeed_job_extract
from extractors.jobkorea import extract_jobkorea_jobs
from file import save_to_file

app = Flask("JobScrapper")
db = {}
dbfl = {}


@app.route("/")
def home():
    return render_template("home.html", name="Ryu")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    location = request.args.get("location")
    if keyword == None or location == None or keyword == "" or location == "":
        return redirect("/")
    if keyword in db and location in dbfl:
        jobs = db[keyword]
        regions = dbfl[location]
    else:
        indeed = indeed_job_extract(keyword, location)
        jobkorea = extract_jobkorea_jobs(keyword)
        jobs = indeed + jobkorea
        db[keyword] = jobs
        regions = str(location)
        dbfl[location] = regions
    return render_template("search.html", keyword=keyword, location=location, jobs=jobs, regions=regions)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    location = request.args.get("location")
    if keyword == None or location == None or keyword == "" or location == "":
        return redirect("/")
    if keyword not in db or location not in dbfl:
        return redirect(f"/search?keyword={keyword}&location={location}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run("127.0.0.1")
