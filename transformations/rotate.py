import cv2
from PIL import Image
import imutils as im
from transformations.util.transformacaoPIL2CV2 import tranformarPIl2CV2

def rotate(pilImagem, rotacao):
    
    img = tranformarPIl2CV2(pilImagem)

    imgRotate = im.rotate(img, angle=rotacao)

    # Converte de volta para PIL
    # Detecta o número de canais para definir o modo correto
    if len(imgRotate.shape) == 2:  # Imagem em escala de cinza
        pilImagem = Image.fromarray(imgRotate, mode='L')
    elif imgRotate.shape[2] == 3:  # Colorida RGB/BGR
        pilImagem = Image.fromarray(cv2.cvtColor(imgRotate, cv2.COLOR_BGR2RGB), mode='RGB')
    else:
        raise ValueError("Formato de imagem não suportado")

    return pilImagem
