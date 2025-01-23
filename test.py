<<<<<<< HEAD
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
=======
>>>>>>> 3ea4228bc8653afaa50cccb2a5cbf33304d4116c
