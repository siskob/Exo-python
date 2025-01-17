chemin = r"C:\Users\bsissoko\Documents\Exo-python\JSON\fichier_texte"

with open(chemin, "r") as f :
    contenu = f.read() # Va lire le fichier exactement comme il est.
    #repr(f.read()) : mettre sur une ligne ou f.read().readlines() : une ligne mais détacher ou read().splitlines() 
    print(contenu)