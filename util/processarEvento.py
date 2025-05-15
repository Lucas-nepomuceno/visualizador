from transformations.escalaCinza import escala_cinza
from transformations.inverterCores import inverterCores
from transformations.detBordas import detBordas
from transformations.blur import blur
from transformations.nitidez import nitidez
from transformations.contraste import contraste
from transformations.windowRed import redimensionar
from transformations.rotate import rotate

def processar_evento(event, img, escala = 0):

    match event:
        
        case '-BTCI-':
            imagem_processada = escala_cinza(img)
            return imagem_processada
        case '-BTI-':
            imagem_processada = inverterCores(img)
            return imagem_processada
        case '-BTDES-':
            imagem_processada = blur(img, escala)
            return imagem_processada
        case '-BTN-':
            imagem_processada = nitidez(img, escala)
            return imagem_processada
        case '-BTDET-':
            imagem_processada = detBordas(img)
            return imagem_processada
        case '-BTCO-':
            imagem_processada = contraste(img, escala)
            return imagem_processada
        case '-BTRE-':
            imagem_processada = redimensionar(img)
            return imagem_processada or img
        case '-BTRO-':
            imagem_processada = rotate(img, escala)
            return imagem_processada
        case _:
            return img