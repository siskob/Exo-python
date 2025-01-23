from pathlib import Path

tri_dir = {
            ".mp3" : "Musique",
            ".wav" : "Musique",
            ".flac" : "Musique",
            ".avi" : "Videos",
            ".mp4" : "Videos",
            ".gif" : "Videos",
            ".bmp" : "Images",
            ".png" : "Images",
            ".jpg" : "Images",
            ".txt" : "Documents",
            ".pptx" : "Documents",
            ".csv" : "Documents",
            ".xls" : "Documents",
            ".odp" : "Documents",
            ".pages" : "Documents"
}

chemin = Path("C:\\Users\\sisso\\Documents\\Exo-python\\data")

# On récupère tous les fichiers dans le dossier de base
files = [f for f in chemin.iterdir() if f.is_file()]

for f in files : 
    #Concaténation entre avec le dossier de base et "files" à partir des extensions contenues dans le dictionnaire
    final = chemin / tri_dir.get(f.suffix, "Autres")
    # On crée le dossier cible s'il n'existe pas déjà
    final.mkdir(exist_ok=True) 
    #Déplacment des fichiers vers le dossier cible en gardant leur nom
    f.rename(final / f.name)


