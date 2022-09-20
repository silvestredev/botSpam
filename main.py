from bs4 import BeautifulSoup
import requests
import pyautogui
import time

def botSpam(url, tag):
    time.sleep(5) #esperar 5s para efetuar o processamento
    req = requests.get(url) 
    parse = BeautifulSoup(req.text, 'html.parser')
    html = parse.find_all(tag)

    for mensagem in html:
        pyautogui.typewrite(mensagem.get_text())
        pyautogui.press('enter')


botSpam('https://www.pensador.com/frases_de_rap/', 'p')