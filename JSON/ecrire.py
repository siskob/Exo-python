chemin = r"C:\Users\bsissoko\Documents\Exo-python\JSON\fichier_texte"

with open(chemin, "w") as f : # open(chemin, "a" : pour ajouter à la fin du fichier sans écraser)
    f.write("\nBonjour") #Ecrase tout ce qui était dans le fichier