import numpy as np
import face_recognition
import cv2
import certifi
import urllib3

video = cv2.VideoCapture(0)

foto_pessoa = face_recognition.load_image_file("pessoa.jpg")
cod_rosto_pessoa = face_recognition.face_encodings(foto_pessoa)[0]

cod_rostos_conhecidos = [
    cod_rosto_pessoa
]
cod_rostos_nomes = [
    '2' #ID para usuario "Pessoa"
]

locais_rostos = []
cod_rostos = []
nomes_rostos = []

processar_quadro = True

url = 'https://api.thingspeak.com/update?api_key=6Z31LU6UTERF5E0R&field1=' #Link ThingSpeak com Chave de Escrita do canal
nome = ''

while True:
    ret, quadro = video.read()

    quadro_redim = cv2.resize(quadro, (0, 0), fx=0.25, fy=0.25)

    quadro_rgb = quadro_redim[:, :, ::-1]

    if processar_quadro:
        locais_rostos = face_recognition.face_locations(quadro_rgb)
        cod_rostos = face_recognition.face_encodings(quadro_rgb, locais_rostos)

        nomes_rostos = []
        for rosto_cod in cod_rostos:
            corresp = face_recognition.compare_faces(cod_rostos_conhecidos, rosto_cod)
            nome = '5' #ID para "Desconhecido"

            if True in corresp:
                primeira_corresp = corresp.index(True)
                nome = cod_rostos_nomes[primeira_corresp]

            nomes_rostos.append(nome)
            
            if nome != '':
                http = urllib3.PoolManager(
                    cert_reqs='CERT_REQUIRED',
                    ca_certs=certifi.where())
                response = http.request('GET', url + str(nome))
                print(nome)
            else:
                continue

    processar_quadro = not processar_quadro
	
video.release()
cv2.destroyAllWindows()