from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gryffindor")
def griffendor():
    return render_template("griffindor.html")


@app.route("/slytherin")
def slytherin():
    return render_template("slytherin.html")

@app.route("/ravenclaw")
def ravenclaw():
    return render_template("ravenclaw.html")

@app.route("/hufflepuff")
def hufflepuff():
    return render_template("hufflepuff.html")

app.run(debug=True)