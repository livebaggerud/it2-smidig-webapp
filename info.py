import requests as req

def hent_navn():
    url = "https://hp-api.onrender.com/api/characters"
    repons = req.get(url, headers = {"User-agent":"Lives mac"})
    data = repons.json()
    for karakter in data:
        navn = karakter["name"]
        print(navn)

def hent_gryffindor():
    url = "https://hp-api.onrender.com/api/characters"
    repons = req.get(url, headers = {"User-agent":"Lives mac"})
    data = repons.json()
    for karakter in data:
        if karakter["house"] == "Gryffindor":
            hent_navn()

def hent_slytherin():
    url = "https://hp-api.onrender.com/api/characters"
    repons = req.get(url, headers = {"User-agent":"Lives mac"})
    data = repons.json()
    for karakter in data:
        if karakter["house"] == "Slytherin":
            hent_navn()

def hent_hufflepuff():
    url = "https://hp-api.onrender.com/api/characters"
    repons = req.get(url, headers = {"User-agent":"Lives mac"})
    data = repons.json()
    for karakter in data:
        if karakter["house"] == "Hufflepuff":
            hent_navn()

def hent_ravenclaw():
    url = "https://hp-api.onrender.com/api/characters"
    repons = req.get(url, headers = {"User-agent":"Lives mac"})
    data = repons.json()
    for karakter in data:
        if karakter["house"] == "Ravenclaw":
            hent_navn()

