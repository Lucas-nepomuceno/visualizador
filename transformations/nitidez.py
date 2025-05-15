import cv2
from PIL import Image
from transformations.util.transformacaoPIL2CV2 import tranformarPIl2CV2

def nitidez(pilImagem, escala):
    
    img = tranformarPIl2CV2(pilImagem)

    #Creditos OPENCV: https://www.opencvhelp.org/tutorials/image-processing/how-to-sharpen-image/

    # Apply Gaussian blur
    imgBlur = cv2.GaussianBlur(img, (51, 51), 1)
    # Subtract the blurred image from the original
    high_pass = cv2.subtract(img, imgBlur)
    # Add the high-pass image back to the original
    imgNitida = cv2.addWeighted(img, 1.0, high_pass, escala, 0)

    # Converte de volta para PIL
    # Detecta o número de canais para definir o modo correto
    if len(imgNitida.shape) == 2:  # Imagem em escala de cinza
        pilImagem = Image.fromarray(imgNitida, mode='L')
    elif imgNitida.shape[2] == 3:  # Colorida RGB/BGR
        pilImagem = Image.fromarray(cv2.cvtColor(imgNitida, cv2.COLOR_BGR2RGB), mode='RGB')
    else:
        raise ValueError("Formato de imagem não suportado")

    return pilImagem
