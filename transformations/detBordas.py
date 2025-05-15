import cv2
from PIL import Image
from transformations.util.transformacaoPIL2CV2 import tranformarPIl2CV2

def detBordas(pilImagem):
    
    img = tranformarPIl2CV2(pilImagem)

    imgBordas = cv2.Sobel(img, -1, 1, 1)

    # Detecta o número de canais para definir o modo correto
    if len(imgBordas.shape) == 2:  # Imagem em escala de cinza
        pilImagem = Image.fromarray(imgBordas, mode='L')
    elif imgBordas.shape[2] == 3:  # Colorida RGB/BGR
        pilImagem = Image.fromarray(cv2.cvtColor(imgBordas, cv2.COLOR_BGR2RGB), mode='RGB')
    else:
        raise ValueError("Formato de imagem não suportado")

    return pilImagem
