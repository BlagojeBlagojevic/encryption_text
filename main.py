import PySimpleGUI as sg
from cryptography.fernet import Fernet
import base64

text=''

def encode(zakodiranje,key,):
   if len(key)==32:
        key1 = base64.urlsafe_b64encode(bytes(key, 'uTF-8'))
        fernet=Fernet(key1)
        poruka = fernet.encrypt(bytes(zakodiranje,'UTF-8'))
        print(poruka)
        return poruka
   else:
       return 'NIJE 32 KARAKTERA!!!'
#ASDASDASDASDASDASDASDASDASDASDAS
def decode(key,cliphertext):
    if len(key)==32:
        key1 = base64.urlsafe_b64encode(bytes(key, 'uTF-8'))
        fernet = Fernet(key1)
        decMessage = fernet.decrypt(cliphertext)
        return decMessage
    else:
        return 'NIJE 32 KARAKTERA!!!'

sg.theme('DarkAmber')
layout_start=[
        [sg.Text("Unesi kod(32 karaktera): "),sg.InputText(key='-KEY_U-')],
        [sg.Text("Unesite tekst za desifrovanje",),sg.InputText(key='-DESIFROVANJE-'),],
        [sg.Button("Desifruj")],
        [sg.Text("Unesi kod(32 karaktera): "), sg.InputText(key='-KEY_D-')],
        [sg.Text("Unesite tekst za sifrovanje", ), sg.InputText(key='-SIFROVANJE-'), ],
        [sg.Button("Sifruj")],
        ]

window_start=sg.Window(title="Nesto",layout=layout_start)


while True:
    event,value= window_start.read()
    if event=="Sifruj":
        text=encode(value['-SIFROVANJE-'],value['-KEY_D-'])
        layout_display = [[sg.Text(text)]]
        window_display = sg.Window(title="Nesto", layout=layout_display)
        window_display.read()

    if event=="Desifruj":
        text1=decode(value['-KEY_U-'],value['-DESIFROVANJE-'])
        layout_display1 = [[sg.Text(text1)]]
        window_display = sg.Window(title="Nesto", layout=layout_display1)
        window_display.read()
