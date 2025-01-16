import random

print("Bienvenue au jeu de combat. Vous avez 50 points de vie chacun pour commencer\n")

point_de_vie_restant = 50
point_de_vie_restant_ennemi = 50

nbre_potion = 3
   
while True :
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?: ")
    if not choix.isdigit() :
      print("Desolez, vous devez rentrer un nombre valide") 
    elif int(choix) < 1 or int(choix)>2 :
        print("Entrez (1) ou (2)")
    elif int(choix) == 1 :
        attaquer_ennemi = random.randint(5, 10)#J'attaque l'ennemi
        attaque_adverse = random.randint(5, 15)#L'ennemi attaque
        print(f"Vous avez infligé {attaquer_ennemi} points à l'ennemi")
        print(f"L'ennemi vous a infligé {attaque_adverse} points\n")
        point_de_vie = point_de_vie_restant - attaque_adverse
        point_de_vie_restant = point_de_vie
        print(f"Il vous reste {point_de_vie_restant} points de vie")
        point_de_vie_ennemi = point_de_vie_restant_ennemi - attaquer_ennemi
        point_de_vie_restant_ennemi = point_de_vie_ennemi
        print(f"Il reste {point_de_vie_restant_ennemi} points de vie à l'ennemi\n")
        print("----------------------------------")

        if (point_de_vie_restant_ennemi <= 0 and point_de_vie_restant > 0) or (point_de_vie_restant_ennemi < point_de_vie_restant < 0):
            print("Félicitation ! Vous avez remporté la partie")
            break
        elif (point_de_vie_restant <= 0 and point_de_vie_restant_ennemi > 0) or (point_de_vie_restant < point_de_vie_restant_ennemi < 0) :
            print("Game over ! Vous avez perdu")
            break
    elif int(choix) == 2 and nbre_potion > 0 :
        potion = random.randint(15, 50)
        nbre_potion -= 1
        point_de_vie_restant = point_de_vie_restant + potion
        print(f"Vous avez à present {point_de_vie_restant} points de vie")
        attaque_adverse = random.randint(5, 15)
        print(f"L'ennemi vous a infligé {attaque_adverse} points\n")
        point_de_vie = point_de_vie_restant - attaque_adverse
        point_de_vie_restant = point_de_vie
        print(f"Il vous reste {point_de_vie_restant} points de vie")
        print(f"Il reste {point_de_vie_restant_ennemi} points de vie à l'ennemi\n")
        print("----------------------------------")

        if (point_de_vie_restant_ennemi <= 0 and point_de_vie_restant > 0) or (point_de_vie_restant_ennemi < point_de_vie_restant < 0):
            print("Félicitation 🎉🎉🎉 Vous avez remporté la partie")
            break
        elif (point_de_vie_restant <= 0 and point_de_vie_restant_ennemi > 0) or (point_de_vie_restant < point_de_vie_restant_ennemi < 0) :
            print("Game over ! Vous avez perdu")
            break
    elif int(choix) == 2 and nbre_potion <= 0 : 
        print("Désolez vous ne pouvez plus prendre de potion")