import json

chemin = r"C:\Users\bsissoko\Documents\Exo-python\JSON\module_json.json"

with open(chemin, "r") as f : 
    #json.dump(list(range(10)), f, indent=4) Ecrire dans le fichier f
    liste = json.load(f)
    print(liste)