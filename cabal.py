import time
import pyautogui
import subprocess

dg = input("Qual dg deseja fazer?")
qtde = int(input("Quantas vezes deseja fazer?"))

for i in range(qtde):
# Seleciona dg
    match dg:
        case 'caos 1':
            time.sleep(2)
            pyautogui.moveTo(730, 266)
            time.sleep(1)
            pyautogui.click(730, 266)
            time.sleep(4)

            pyautogui.moveTo(680,210)
            time.sleep(1)
            pyautogui.click(680, 210)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
            subprocess.call("caos_dentro.py", shell=True)
        case 'caos 2':
            time.sleep(2)
            pyautogui.moveTo(730, 266)
            time.sleep(1)
            pyautogui.click(730, 266)
            time.sleep(4)

            pyautogui.moveTo(680,230)
            time.sleep(1)
            pyautogui.click(680, 230)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
            subprocess.call("caos_dentro.py", shell=True)
        case 'caos 3':
            time.sleep(2)
            pyautogui.moveTo(730, 266)
            time.sleep(1)
            pyautogui.click(730, 266)
            time.sleep(4)

            pyautogui.moveTo(680,250)
            time.sleep(1)
            pyautogui.click(680, 250)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
            subprocess.call("caos_dentro.py", shell=True)
        case 'caos 4':
            time.sleep(2)
            pyautogui.moveTo(730, 266)
            time.sleep(1)
            pyautogui.click(730, 266)
            time.sleep(4)

            pyautogui.moveTo(680,270)
            time.sleep(1)
            pyautogui.click(680, 270)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
            subprocess.call("caos_dentro.py", shell=True)
        case 'caos 5':
            time.sleep(2)
            pyautogui.moveTo(730, 266)
            time.sleep(1)
            pyautogui.click(730, 266)
            time.sleep(4)

            pyautogui.moveTo(680,290)
            time.sleep(1)
            pyautogui.click(680, 290)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
            subprocess.call("caos_dentro.py", shell=True)
        case 'caos 6':
            time.sleep(2)
            pyautogui.moveTo(730, 266)
            time.sleep(1)
            pyautogui.click(730, 266)
            time.sleep(4)

            pyautogui.moveTo(680,310)
            time.sleep(1)
            pyautogui.click(680, 310)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
            subprocess.call("caos_dentro.py", shell=True)
        case other:
            print('DG não encontrada')

# roda dado
    dado = pyautogui.locateOnScreen('dado.png', confidence=0.9)
    dado = pyautogui.center(dado)
    dadox, dadoy = dado
    pyautogui.click(dadox, dadoy)
    time.sleep(3)

# sair da dg
    sair = pyautogui.locateOnScreen('sair.png', confidence=0.9)
    sair = pyautogui.center(sair)
    sairx, sairy = sair
    pyautogui.click(sairx, sairy)
    time.sleep(3)