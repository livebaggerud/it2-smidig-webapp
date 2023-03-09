from flask import Flask, render_template
from info import hent_gryffindor 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gryffindor")
def griffendor():
    gryffendor_karakter = hent_gryffindor()
    return render_template("griffindor.html", gryffendor_karakter = gryffendor_karakter)


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