import cv2
import numpy as np
from PIL import Image
from transformations.util.transformacaoPIL2CV2 import tranformarPIl2CV2

def contraste(pilImagem, escala):
    
    img = tranformarPIl2CV2(pilImagem)

    #Creditos GeeksForGeeks:https://www.geeksforgeeks.org/image-enhancement-techniques-using-opencv-python/
 
    imgCon = cv2.addWeighted(img, escala, np.zeros(img.shape, img.dtype), 0, 0)


    # Converte de volta para PIL
    # Detecta o número de canais para definir o modo correto
    if len(imgCon.shape) == 2:  # Imagem em escala de cinza
        pilImagem = Image.fromarray(imgCon, mode='L')
    elif imgCon.shape[2] == 3:  # Colorida RGB/BGR
        pilImagem = Image.fromarray(cv2.cvtColor(imgCon, cv2.COLOR_BGR2RGB), mode='RGB')
    else:
        raise ValueError("Formato de imagem não suportado")

    return pilImagem
