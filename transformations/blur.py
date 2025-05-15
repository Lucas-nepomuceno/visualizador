import cv2
from PIL import Image
from transformations.util.transformacaoPIL2CV2 import tranformarPIl2CV2

def blur(pilImagem, escala):
    
    img = tranformarPIl2CV2(pilImagem)

    imgBlur = cv2.GaussianBlur(img, (escala, escala), 0)

    # Converte de volta para PIL
    # Detecta o número de canais para definir o modo correto
    if len(imgBlur.shape) == 2:  # Imagem em escala de cinza
        pilImagem = Image.fromarray(imgBlur, mode='L')
    elif imgBlur.shape[2] == 3:  # Colorida RGB/BGR
        pilImagem = Image.fromarray(cv2.cvtColor(imgBlur, cv2.COLOR_BGR2RGB), mode='RGB')
    else:
        raise ValueError("Formato de imagem não suportado")

    return pilImagem
