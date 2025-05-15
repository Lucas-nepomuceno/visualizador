import FreeSimpleGUI as sg

sg.theme('DarkAmber')

colunaEdicao = [
        [sg.Text("Edite sua foto", key='-ED-', visible=False, justification='left')],
        [sg.Button('Redimensione a imagem', key='-BTRE-', visible=False, button_color=('white', 'darkblue'))],
        [sg.Checkbox("Escala de Cinza", key='-BTCI-', visible=False, enable_events=True)],
        [sg.Checkbox("Inversão", key='-BTI-', visible=False, enable_events=True)],
        [sg.Checkbox("Detecção de Bordas", key='-BTDET-', visible=False, enable_events=True)],
        [sg.Text("Blur:", visible=False, key='-BLT-'), sg.Slider(range=(1, 31), resolution=2, orientation='h', size=(20, 15), key='-BTDES-', tooltip='Arraste para ajustar', visible=False, enable_events=True)],
        [sg.Text("Nitidez:", visible=False, key='-NIT-'), sg.Slider(range=(1, 31), resolution=2, orientation='h', size=(20, 15), key='-BTN-', tooltip='Arraste para ajustar', visible=False, enable_events=True)],
        [sg.Text("Contraste:", visible=False, key='-COT-'), sg.Slider(range=(1, 1.5), resolution=0.01, orientation='h', size=(20, 15), key='-BTCO-', tooltip='Arraste para ajustar', visible=False, enable_events=True)],
        [sg.Text("Rotação:", visible=False, key='-TRO-'), sg.Slider(range=(0, 360), resolution=1, orientation='h', size=(20, 15), key='-BTRO-', tooltip='Arraste para ajustar', visible=False, enable_events=True)],
    ]
