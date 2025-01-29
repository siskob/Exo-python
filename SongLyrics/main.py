from pprint import pprint

import requests

def get_all_urls():
    page_number = 1
    links = []
    while True :
        r = requests.get(f"https://genius.com/api/artists/29743/songs?page={page_number}&sort=popularity") 
        if r.status_code == 200 : # Si on n'arrive pas à joindre l'url
            response = r.json().get("response", {}) # Pour ne pas avoir d'erreur si on trouve pas response
            next_page = response.get("next_page") # Récupérer la page suivante contenu dans response
            
            page_number += 1

        if not next_page :
            print("No more page to fetch.")
            break


get_all_urls()
