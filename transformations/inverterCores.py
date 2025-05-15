import cv2
from PIL import Image
from transformations.util.transformacaoPIL2CV2 import tranformarPIl2CV2

def inverterCores(pilImagem):
    
    img = tranformarPIl2CV2(pilImagem)

    imgInvert = cv2.bitwise_not(img)

    # Converte de volta para PIL
    # Detecta o número de canais para definir o modo correto
    if len(imgInvert.shape) == 2:  # Imagem em escala de cinza
        pilImagem = Image.fromarray(imgInvert, mode='L')
    elif imgInvert.shape[2] == 3:  # Colorida RGB/BGR
        pilImagem = Image.fromarray(cv2.cvtColor(imgInvert, cv2.COLOR_BGR2RGB), mode='RGB')
    else:
        raise ValueError("Formato de imagem não suportado")

    return pilImagem
