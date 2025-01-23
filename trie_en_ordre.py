
chemin = "C:\\Users\\sisso\\Documents\\Exo-python\\prenoms.txt"

with open(chemin, "r") as f :
    contenu = f.read() # Va lire le fichier exactement comme il est.
        
# Remplacer les sauts de ligne et les points par des virgules
    contenu_normalise = contenu.replace("\n", ",").replace(".", ",")

# Diviser le contenu en utilisant les virgules comme séparateurs
    elements_bruts = contenu_normalise.split(",")

# Créer une nouvelle liste où chaque élément est nettoyé des espaces superflus
    liste_noms = []
    for element in elements_bruts:
        nom = element.strip()  # Supprimer les espaces avant et après
        if nom:  # Vérifier si le nom n'est pas une chaîne vide
            liste_noms.append(nom)

    liste_noms =sorted(liste_noms)

# Chemin vers le fichier où enregistrer les résultats
chemin_fichier = "C:\\Users\\sisso\\Documents\\Exo-python\\prenoms_tries.txt"
print(chemin_fichier)

# Écrire les éléments dans le fichier, un par ligne
with open(chemin_fichier, "w", encoding="utf-8") as fichier:
    for nom in liste_noms:
        fichier.write(nom + "\n")
