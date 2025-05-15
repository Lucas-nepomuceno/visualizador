import cv2
from PIL import Image
from transformations.util.transformacaoPIL2CV2 import tranformarPIl2CV2

def escala_cinza(pilImagem):
    
    if pilImagem.mode != 'L':

        img = tranformarPIl2CV2(pilImagem)

        # Converte RGB -> Grayscale direto (sem passar por BGR)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Converte de volta para PIL
        pilImagem = Image.fromarray(imgGray, mode='L')

    return pilImagem
