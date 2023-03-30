from flask import Flask, render_template
from info import hent_gryffindor 
from info import hent_slytherin
from info import hent_hufflepuff
from info import hent_ravenclaw

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
    slytherin_karakterer = hent_slytherin()
    return render_template("slytherin.html", slytherin_karakterer = slytherin_karakterer)

@app.route("/ravenclaw")
def ravenclaw():
    ravenclaw_karakterer = hent_ravenclaw()
    print(ravenclaw_karakterer)
    return render_template("ravenclaw.html", ravenclaw_karakterer = ravenclaw_karakterer)


@app.route("/hufflepuff")
def hufflepuff():
    hufflepuff_karakterer = hent_hufflepuff()
    return render_template("hufflepuff.html", hufflepuff_karakterer = hufflepuff_karakterer)

app.run(debug=True)