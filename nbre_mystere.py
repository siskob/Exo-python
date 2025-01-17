import random

def jeu_de_nbre_mystere():
	print("Bienvenue dans le jeu de nombre mystère !")
	print("Je vais penser à un nombre entre 1 et 100. Tu devras devinez en 5 essaies maxi ce nombre")

	nbre_aleatoire = random.randint(0, 100)
	essaie_restant = 5

	while essaie_restant > 0:
		choix = input(f"Devinez le nombre (il vous reste {essaie_restant} essaies): ")
		
		if not choix.isdigit() :
			print("Veuillez entrez un nombre s'il vous plait")
		
		elif int(choix) == nbre_aleatoire :
			print("Félicitation vous avez devinez juste 🎉🎉🎉")
			break
			
		
		elif int(choix) < nbre_aleatoire:
			print(f"Le nombre mystère est plus grand que {choix}")
		else :
			print(f"Le nombre mystère est plus petit que {choix}")
		essaie_restant -= 1
		
	if essaie_restant == 0 and int(choix) != nbre_aleatoire :
		print(f"Dommage ! Vous avez épuisez toutes vos chances. Le nombre mstère était : {nbre_aleatoire}")
	print("Merci de votre participation")

if __name__ == "__main__":
    jeu_de_nbre_mystere()
            