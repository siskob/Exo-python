import json
import sys
import os


#Chemin du dossier courant
CUR_DIR = os.path.dirname(__file__)

#Chemin du fichier liste.json
chemin_fichier = os.path.join(CUR_DIR, "liste.json") #joindre les 2 chemins : /liste.json

liste_course = []
selection = [
 "Ajouter un élément à la liste de courses",
 "Retirer un élément de la liste de courses" , 
 "Afficher les éléments de la liste de courses", 
 "Vider la liste de courses",
 "Quitter le programme"
]

longueur = len(selection)

if os.path.exists(chemin_fichier):#Verifier si un chemin existe
    with open(chemin_fichier, "r") as f :
        liste_course = json.load(f)#Ouvrir et lire le contenu
else:
    liste_course = []

print(f"Choisissez parmi les {longueur} options suivantes : ")

while True:
    for i, element in enumerate(selection, 1):
        print(f"{i}. {element}")
    choix = input("Votre choix : ")
    if not (choix.isdigit() and int(choix) in range(1, longueur + 1)):
        print(f"Non valide, choisissez parmi les {longueur} options suivantes : ")
        continue
    
    choix = int(choix) 
#Ajouter un élément à la liste de courses
    if choix == 1:
        ajouter = input("Entrez le nom d'un élément à ajouter à la liste : ")
        liste_course.append(ajouter)
        print(f"L'élément {ajouter} a été ajouté à la liste")
        print("------------------------------------")
        with open(chemin_fichier,"w") as f:
            json.dump(liste_course, f)
        continue

        
        
#Retirer un élément de la liste de courses
    elif choix == 2:
        element_a_retire = input("Entrez le nom de l'élément à retirer : ")
        if element_a_retire in liste_course :
            liste_course.remove(element_a_retire)
            print(f"L'élément {element_a_retire} a été retiré de la liste")
            with open(chemin_fichier,"w") as f:
                json.dump(liste_course, f) #Enregistrer le contenu de la liste dans le fichier json
            continue

        else:
            print("Votre élément n'est pas présent dans la liste de course") 
            print("------------------------------------")
            
        
#Afficher les éléments de la liste de courses           
    elif choix == 3: 
        if liste_course:
            print("Liste de courses : ")
            for i, element in enumerate(liste_course, 1): 
                print(f"{i}. {element}")  
            print("\n-----------------------------------")           
        else:
            print("La liste de courses est vide.")
            print("\n-----------------------------------")
                 
#Vider la liste de courses
    elif choix == 4:
        liste_course.clear()
        print("La liste à été vidée")
        print("\n-----------------------------------")
             
#Quitter le programme           
    elif choix == 5:
        if os.path.exists(chemin_fichier):#Verifier si un chemin existe
            with open(chemin_fichier, "w") as f :
                json.dump(liste_course, f)#Enregistrer le contenu de la liste dans le fichier json
        print("Merci d'avoir utilisé le programme. Au revoir!")
        sys.exit()