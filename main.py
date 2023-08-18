from flask import Flask, render_template

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="Ryu")


@app.route("/hello")
def hello():
    return "<h1>hello there</h1>"


app.run("127.0.0.1")
