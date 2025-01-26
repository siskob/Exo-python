
try:
    fichier = input("Entrez un fichier à ouvrir : ")

        #Ouvrir le fichier pour lire son contenu
    with open(fichier, "r") as f:
            contenu = f.read()
            print(contenu)
except UnicodeDecodeError :
    print("Erreur : Impossible d'ouvrir le fichier")
except FileNotFoundError:
     print("Erreur : Le fichier est introuvable")
