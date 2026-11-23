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
    visages = fr.face_encodings(image)
    positions = fr.face_locations(image)

    for visage, position in zip(visages, positions):
        visage_test = fr.compare_faces(encoding_connues, visage)

        if True in visage_test:
            index = visage_test.index(True)
            nom = noms_connues[index]
        else:
            nom = "Inconnu"

        top, right, bottom, left = position

        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(image, nom, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow("Face Recognition", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_test = input("Quelle image veux-tu analyser ? ")
reconnaitre_visage(image_test)
