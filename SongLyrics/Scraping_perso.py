from pprint import pprint

import requests
from bs4 import BeautifulSoup

def is_valid(mot_valable):
    return "[" not in mot_valable or "]" not in mot_valable

def recuperer_paroles(urls):
    print(f"Contact du site {urls}")
    r = requests.get(urls)
    if r.status_code != 200:
        print("page impossible à récupérer")
        return []
        
    soup = BeautifulSoup(r.content, "html.parser")
    paroles = soup.find("div", class_="Lyrics-sc-37019ee2-1 jRTEBZ")
    if not paroles:
        recuperer_paroles(urls)

    liste_de_mots = []
    for p in paroles.stripped_strings:
        for mot_valable in p.split():
            if is_valid(mot_valable):
                paroles_trier = mot_valable.strip(",").strip(".")
                liste_de_mots.append(paroles_trier)
    return liste_de_mots
    

recuperer_paroles("https://genius.com/Patrick-bruel-place-des-grands-hommes-lyrics")    


def recuperer_url():
    numero_page = 1
    liens = []
    while True:
        r = requests.get(f"https://genius.com/api/artists/29743/songs?page={numero_page}&sort=popularity")
        if r.status_code == 200:
            print(f"Contact de la page {numero_page}")
            response = r.json().get("response")
            page_suivante = response.get("next_page")

            songs = response.get("songs")
            
            for song in songs:
                liens.append(song.get("url"))
            
            numero_page += 1

        if not page_suivante:
            print("Plus de page suivante")
            break

    return liens
    

