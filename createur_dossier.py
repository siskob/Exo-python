from pathlib import Path

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

chemin = Path("C:\\Users\\sisso\\Documents\\Exo-python\\Createur_De_Dossier")

#keys_list = list(d.keys())


# Créer les dossiers pour chaque clé et leurs sous-dossiers
for key, values in d.items():
    # Créer le dossier pour chaque clé
    dossier_cle = chemin / key
    dossier_cle.mkdir(exist_ok=True)

    # Créer les sous-dossiers pour chaque valeur associée à la clé
    for value in values:
        sous_dossier = dossier_cle / value
        sous_dossier.mkdir(exist_ok=True)



