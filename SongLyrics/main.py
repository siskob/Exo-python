import json
import collections
from pprint import pprint

import requests
from bs4 import BeautifulSoup

#Ne pas afficher les refrain entre crochets
def is_valid(word):
    return "[" not in word and "]" not in word #Va retourner True si c'est vrai

#Récupérer les paroles 
def extract_lyrics(url):
    print(f"Fetching lyrics{url}") #Pour avoir un feedback de l'url à chaque fois
    r = requests.get(url) # Contacter l'url
    #print(r.status_code) pour voir le statut
    if r.status_code != 200 :
        print("page impossible à récupérer")
        return []
    
    soup = BeautifulSoup(r.content, 'html.parser') #pour en extraire des informations ou vérifier sa validité
    lyrics = soup.find("div", class_ ="Lyrics-sc-37019ee2-1 jRTEBZ")
    if not lyrics : 
        return extract_lyrics(url)
    
    all_words = [] #La liste va contenir tous les mots de longueur suppérieure à 2
    for sentence in lyrics.stripped_strings : #Pour retirer les balises et retenir uniquement les paroles 
        #words.extend(sentence.split()) #Metrre les paroles dans une liste et découper les mots pour une grande liste

# les mots et pas de réfrain (entre crochets)
        sentence_words = [word.strip(",").strip(".").lower() for word in sentence.split() if is_valid(word)] 
        all_words.extend(sentence_words)

    return all_words


#Récupérer les urls
def get_all_urls():
    page_number = 1
    links = []
    while True :
        r = requests.get(f"https://genius.com/api/artists/29743/songs?page={page_number}&sort=popularity") 
        if r.status_code == 200 : # Si on n'arrive pas à joindre l'url
            print(f"Fetching page {page_number}") #Pour avoir un feedback du la page à chauqe fois
            response = r.json().get("response", {}) # Pour ne pas avoir d'erreur si on trouve pas response
            next_page = response.get("next_page") # Récupérer la page suivante contenu dans response
            
            songs = response.get("songs") # Récupérer les chansons dans responses
            for song in songs: # Boucler sur les chansons
                links.append(song.get("url")) # Récupérer les url de chaque chanson et Ajouter les url à la liste links
            
            page_number += 1

        if not next_page :
            print("No more page to fetch.")
            break
    return links


def get_all_words():#Pour récupérer les paroles de toutes les chansons sur toutes les urls
    urls = get_all_urls()
    words = [] # Giga grande liste qui doit contenir toutes les paroles
    for url in urls: #Boucler sur toutes les urls
        lyrics = extract_lyrics(url=url) #Extraire les paroles de chaque url
        words.extend(lyrics) 

#Ecrire dans un fichier pour éviter de chaque fois lancer le script
    with open("data1.json", "w") as f:
        json.dump(words, f, indent = 4)

    # with open("C:\\Users\\bsissoko\\Documents\\Exo-python\\SongLyrics\\data1.json", "r") as f:
    #     words = json.load(f)

    counter = collections.Counter(w for w in words if len(w) > 3) #Compter les mots et garder ceux > 5 caract
    most_common_words =  counter.most_common(15) #Seulement les 15 premiers les plus communs
    pprint(most_common_words)

get_all_words()



#extract_lyrics(url = "https://genius.com/Patrick-bruel-elle-mregardait-comme-ca-lyrics") test avec 1

