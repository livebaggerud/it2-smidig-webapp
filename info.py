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
    griffendor_karakter = []
    for karakter in data:
        if karakter["house"] == "Gryffindor":
            griffendor_karakter.append(karakter)
    
    return griffendor_karakter

def hent_slytherin():
    url = "https://hp-api.onrender.com/api/characters"
    repons = req.get(url, headers = {"User-agent":"Lives mac"})
    data = repons.json()
    slytherin_kar = []
    for karakter in data:
        if karakter["house"] == "Slytherin":
            slytherin_kar.append(karakter)
    
    return slytherin_kar

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

