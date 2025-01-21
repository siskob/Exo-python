<<<<<<< HEAD
dictionnaire = {"prenom": "Paul", 
                "possession": "Ingénieur", 
                "ville": "Paris"}

for cle, valeur in dictionnaire.items() :
    print(cle, valeur)
=======
from pathlib import Path


tri_dir = {
            "mp3" : "Musique",
            "wav" : "Musique",
            "flac" : "Musique",
            "avi" : "Videos",
            "mp4" : "Videos",
            "gif" : "Videos",
            "bmp" : "Images",
            "png" : "Images",
            "jpg" : "Images",
            "txt" : "Documents",
            "pptx" : "Documents",
            "csv" : "Documents",
            "xls" : "Documents",
            "odp" : "Documents",
            "pages" : "Documents"
}

chemin = Path.home()


files = [f for f in chemin.iterdir() if f.is_file()]

for f in files : 
    final = chemin / tri_dir.get(f.suffix, "Divers")
    final.mkdir(exist_ok=True)
    f.rename(final / f.name)
>>>>>>> 97a10c13642e053c97fc59e872ec881b3a686dc8
