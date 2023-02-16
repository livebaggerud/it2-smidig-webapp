from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gryffindor")
def griffendor():
    return render_template("griffindor.html")


@app.route("/slytherin")
def func():
    return render_template("slytherin.html")

app.run(debug=True)