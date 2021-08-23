import pywhatkit as kit
import PySimpleGUI as sg

def success():
    tema = sg.theme('Reddit')
    layout = [
        [sg.Text('Success',font='Roboto')],[sg.Button('Exit',key='btn', auto_size_button=(50,50))]
    ]
    janela = sg.Window('Success',layout,size=(100,70))
    while True:
        event, values = janela.Read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'btn':
            break
    janela.Close()
    
tema = sg.theme('Reddit')
layout = [
    [sg.Text('Write:',font='Roboto',justification='right')],
    [sg.Input(key='int')],
    [sg.Button('Confirm',key='btn')]
]
janela = sg.Window('Escrita',layout,size=(200,150))
while True:
    event, values = janela.Read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'btn':
        kit.text_to_handwriting(values['int'])
        success()
        

janela.Close()