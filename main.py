import os
import cv2
from filters import grayscale, blur

input_dir = 'data/imgs'
files = os.listdir(input_dir)
print(files)
for f in files:
    file_path = f"{input_dir}/{f}"
    # 1. Ouvrir le fichier => extraire l'image qui se trouve dedans
    # image => c'est l'image de base NON filtrée
    image = cv2.imread(file_path)

    # 2. Applique mon filtre
    # En input => j'ai l'image brute
    # En résultat => j'ai l'image en N&B
    image = grayscale.filter_grayscale(image)
    # En input => j'ai l'image en N&B
    # En résultat => j'ai l'image en N&B + floutée
    image = blur.filter_blur(image)

    # 3. Enregistrer l'image filtrée dans le dossier de sortie
    cv2.imwrite(f"data/output/{f}", image)