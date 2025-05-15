import cv2
from PIL import Image
import numpy as np

def tranformarPIl2CV2(pilImagem):
    
    pilImagem = pilImagem.convert('RGB')
    # Converte PIL -> numpy array (formato RGB)
    rgbImg = np.array(pilImagem)
    # Converte RGB -> Grayscale direto (sem passar por BGR)
    imgCV2 = cv2.cvtColor(rgbImg, cv2.COLOR_RGB2BGR)

    return imgCV2