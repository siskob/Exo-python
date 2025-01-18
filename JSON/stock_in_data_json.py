import json
 
with open("data.json", "r") as f : 
    donnees = json.load(f) #Lire le contenu de mon fichier data.json

donnees.append(4) #Ajouter 4 à ce qui est lu

with open("data.json", "w") as f : 
    json.dump(donnees, f, indent=4) #Ecraser l'ancien par le nouveau | (..., ensure_ascii=False): pour correction de l'affichage