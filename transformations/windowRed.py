import FreeSimpleGUI as sg
from PIL import Image

def redimensionar(img):
    imgRatio = img.size[0] / img.size[1]
    print(img.size)

    layout = [
        [sg.Text("Qual o tamanho desejado?")],
        [sg.Text("Largura:"), sg.Input('', size=(7,1), key='-W-', enable_events=True), 
         sg.Text('Altura:'), sg.Input('', size=(7,1), key='-H-', enable_events=True)],
        [sg.Button('Redimensionar'), sg.Button('Cancelar')]
    ]

    window = sg.Window('Redimensione a imagem', layout)
    w = None
    h = None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancelar'):
            break

        if event == '-W-' and values['-W-']: 
            w = float(values['-W-'])
            if w > 0:
                h = w / imgRatio
                window['-H-'].update(h)
        
        if event == '-H-' and values['-H-']:
            h = float(values['-H-'])
            if h > 0:
                w = h * imgRatio
                window['-W-'].update(w)
        
        if event == 'Redimensionar':
                if w and h:
                    resized_img = img.copy()
                    resized_img.thumbnail((w,h))
                    window.close()
                    return resized_img
                else:
                    sg.popup_error(f'Erro ao redimensionar: Insira todos os valores')

    window.close()
    return img
