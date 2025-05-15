import FreeSimpleGUI as sg
from PIL import Image
import io
import os
from os.path import join as pjoin
from util.processarEvento import processar_evento
from util.colunaEdicao import colunaEdicao

sg.theme('DarkAmber')

colunaEdicao = colunaEdicao

layout = [  
    [sg.Text('Bem vindo ao Visualizador Paulista de Imagens', key='-IN-')],
    [sg.Text('Comece inserindo sua imagem:', key='-INS-'), 
     sg.In(key='-FILE-', enable_events=True, visible=False),
     sg.FileBrowse(button_text='Insira sua imagem aqui', file_types=(("Image Files", ["*.jpg", ".png", ".jpeg"]),))],
    [sg.Column(colunaEdicao, justification='left', vertical_alignment='top'),
     sg.VSeperator(),
     sg.Push(),
     sg.Column([[sg.Image(key='-IMG-')]]),
     sg.Push()],
    [sg.Text('Tamanho da imagem:', visible=False, key='-TS-'), sg.Text('', key='-W-', visible=False),sg.Text('x', visible=False, key='-x-'), sg.Text('', key='-H-', visible=False)],
    [sg.Button('Sair'),
     sg.Button(button_text='Salvar', key='-BS-', visible=False)]
]

window = sg.Window('Visualizador de Imagens', layout, resizable=True, finalize=True)
bts = ["-BTCI-", "-BTI-", "-BTDES-", "-BTN-", "-BTDET-", "-BTCO-", "-BTRE-", "-BTRO-"]

img = None
imageLocal = None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    bio = io.BytesIO()
    caminho_arquivo = values['-FILE-']
    if event == '-FILE-': # Se um arquivo for selecionado
        if os.path.exists(caminho_arquivo):
            try: # Mensagens de erro se necessário
                # Abrir e converter a imagem em bytes, porque o Image do FreeSimpleGUI é limitado
                img = Image.open(caminho_arquivo)
                imageLocal = img.copy()
                imageLocal.thumbnail((400,400))
                imageLocal.save(bio, format="PNG") # salvar
                window['-IMG-'].update(data=bio.getvalue())

                #invisivibilizar instruções iniciais
                window['-IN-'].update(visible=False)

                #Atualizar texto
                window['-INS-'].update("Escolher outro arquivo")
                window['-W-'].update(img.size[0])
                window['-H-'].update(img.size[1])

                #visibilizar ferramentas
                ferramentas = ['-NIT-','-ED-', '-BLT-', '-COT-', '-TRO-', '-TS-', '-W-','-x-', '-H-', '-BS-']
                for f in ferramentas:
                    window[f].update(visible=True)
                
                for bt in bts:
                    window[bt].update(visible=True)

            except Exception as e:
                sg.popup_error("Erro ao carregar imagem:", e)

    if event in bts or event == '-BS-':
        if event == '-BTRE-':
            imageRes = processar_evento(event, img)
            if imageRes.size != img.size:
                img = img.resize((imageRes.size[0], imageRes.size[1]))
                sg.popup('Redimensionamento feito com sucesso')
                window['-W-'].update(img.size[0])
                window['-H-'].update(img.size[1])
        else:
            desfoque = int(values['-BTDES-'])
            rotacao = int(values['-BTRO-'])
            nitidez = int(values['-BTN-'])
            contraste = float(values['-BTCO-'])

            imgProcessada = imageLocal.copy()

            if values['-BTCI-']:
                imgProcessada = processar_evento('-BTCI-', imgProcessada)

            if values['-BTI-']:
                imgProcessada = processar_evento('-BTI-', imgProcessada)
            
            if values['-BTDET-']:
                imgProcessada = processar_evento('-BTDET-', imgProcessada)

            medidas = {
                '-BTN-': nitidez,
                '-BTDES-': desfoque,
                '-BTRO-': rotacao,
                '-BTCO-': contraste
            }

            for chave, valor in medidas.items():
                imgProcessada = processar_evento(chave, imgProcessada, valor) #aplica as mudanças pontuais

            if event == '-BS-':
                filename = sg.popup_get_file('Save as', save_as=True, no_window=True,     file_types=(("PNG Image", "*.png"),))
                try:
                    if filename:
                        img_resize = imgProcessada.copy()
                        img_resize = imgProcessada.resize((img.size[0], img.size[1]))
                        img_resize.save(filename)
                except Exception as e:
                        sg.popup_error("Erro ao salvar imagem:", e)                   
                
            imgProcessada.save(bio, format="PNG")
            window['-IMG-'].update(data=bio.getvalue())



window.close()
