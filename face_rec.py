import face_recognition as fr
import os
import cv2
from time import sleep

dossier = os.listdir("faces/")
encoding_connues = []
noms_connues = []

for fichier in dossier:
    if fichier.endswith((".jpg", ".jpeg", ".png")):
        image = fr.load_image_file(f"faces/{fichier}")
        encodage = fr.face_encodings(image)

        if len(encodage) > 0:
            encoding_connues.append(encodage[0])
            noms_connues.append(os.path.splitext(fichier)[0])

def reconnaitre_visage(image_test):
    image = fr.load_image_file(image_test)
    visage = fr.face_encodings(image)

    if len(visage) > 0:
        visage_test = fr.compare_faces(encoding_connues, visage[0])

    if True in visage_test:
        position = visage_test.index(True)
        nom = noms_connues[position]
        return nom
    else:
        return "Inconnu"

image_test = input("Quelle image veux-tu analyser ? ")
resultat = reconnaitre_visage(image_test)
print(resultat)
