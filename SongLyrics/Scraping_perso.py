from pprint import pprint
import collections
import json

import requests
from bs4 import BeautifulSoup


def is_valid(word):
    return "[" not in word and "]" not in word


#Récupérer les paroles
def recuperer_paroles(url):
    print(f"Fetching lyrics{url}")
    r = requests.get(url)
    if r.status_code != 200 :
        print("Page impossible à récupérer")
        return []
    
    soup = BeautifulSoup(r.content, 'html.parser')
    parole = soup.find("div", class_="Lyrics-sc-37019ee2-1 jRTEBZ")
    
    if not parole:
        return recuperer_paroles(url)
    

    all_words = [] #La liste va contenir tous les mots
    for sentence in parole.stripped_strings : #Pour retirer les balises et retenir uniquement les paroles     
        sentence_words = [word.strip(",").strip(".").lower() for word in sentence.split() if is_valid(word)] 
        all_words.extend(sentence_words)

    return all_words
        
#recuperer_paroles("https://genius.com/Patrick-bruel-place-des-grands-hommes-lyrics")


#Récupérer les urls
def recupere_urls():
    numero_page = 1
    liens_chansons = []
    
    while True:
        r = requests.get(f"https://genius.com/api/artists/29743/songs?page={numero_page}&sort=popularity")
        
        if r.status_code == 200:
            print(f"Requette vers la page {numero_page}") # Connaitre le nombre de fois qu'on contacte une page.

            response = r.json().get("response")
            page_suivante = response.get("next_page")

            songs = response.get("songs")

            for song in songs:
                liens_chansons.append(song.get("url"))

            numero_page += 1

        if not page_suivante : 
            print("Plus de page suivante")
            break
    return liens_chansons

def recuperer_tous_les_mots():
    urls = recupere_urls()
    words = []
    for url in urls:
        parole = recuperer_paroles(url=url)
        words.extend(parole)
    
    with open("C:\\Users\\bsissoko\\Documents\\Exo-python\\SongLyrics\\fichier.json", "w") as f:
        json.dump(words, f, indent=4)
        

    counter = collections.Counter(w for w in words if len(w)>10)
    most_common_words = counter.most_common(15)
    pprint(most_common_words)


recuperer_tous_les_mots()


