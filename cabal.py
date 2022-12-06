import time
import pyautogui

# skill1
def skill1(): # 4
    pyautogui.moveTo(870, 1000)
    pyautogui.click(870, 1000, button='right')

# skill 2
def skill2(): # 5
    pyautogui.moveTo(905, 1000)
    pyautogui.click(905, 1000, button='right')

# skill3
def skill3(): # 6
    pyautogui.moveTo(945, 1000)
    pyautogui.click(945, 1000, button='right')

# buff1
def buff1(): # 7
    pyautogui.moveTo(980, 1000)
    pyautogui.click(980, 1000, button='right')

# buff2
def buff2(): # 9
    pyautogui.moveTo(1050, 1000)
    pyautogui.click(1050, 1000, button='right')

# buff3
def buff3(): # 0
    pyautogui.moveTo(1095, 1000)
    pyautogui.click(1095, 1000, button='right')

# skill4
def skill4(): # 8
    pyautogui.moveTo(1015, 1000)
    pyautogui.click(1015, 1000, button='right')

# Target mob
def target():
    pyautogui.middleClick()
# Pega item
def pegar():
    pyautogui.scroll(2)

dg = input("Qual dg deseja fazer?")
qtde = int(input("Quantas vezes deseja fazer?"))

for i in range(qtde):

# Clica para selecionar dg
    time.sleep(2)
    pyautogui.moveTo(730,266)
    time.sleep(1)
    pyautogui.click(730, 266)
    time.sleep(4)

# Seleciona dg
    match dg:
        case 'caos 1':
            pyautogui.moveTo(680,210)
            time.sleep(1)
            pyautogui.click(680, 210)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
        case 'caos 2':
            pyautogui.moveTo(680,230)
            time.sleep(1)
            pyautogui.click(680, 230)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
        case 'caos 3':
            pyautogui.moveTo(680,250)
            time.sleep(1)
            pyautogui.click(680, 250)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
        case 'caos 4':
            pyautogui.moveTo(680,270)
            time.sleep(1)
            pyautogui.click(680, 270)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
        case 'caos 5':
            pyautogui.moveTo(680,290)
            time.sleep(1)
            pyautogui.click(680, 290)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
        case 'caos 6':
            pyautogui.moveTo(680,310)
            time.sleep(1)
            pyautogui.click(680, 310)
            time.sleep(3)
            print("DG selecionada: {}".format(dg))
        case other:
            print('DG não encontrada')

# Entra dg se tiver entrada
#     entrar = pyautogui.locateOnScreen('entrar.png', confidence=0.9)
#     entrar = pyautogui.center(entrar)
#     entrarx, entrary = entrar
#     pyautogui.click(entrarx, entrary)
    pyautogui.moveTo(980, 610)
    time.sleep(1)
    pyautogui.click(980, 610)
    time.sleep(5)

# Inicia dg
    inicia = pyautogui.locateOnScreen('inicia.png', confidence=0.9)
    inicia = pyautogui.center(inicia)
    iniciax, iniciay = inicia
    pyautogui.click(iniciax, iniciay)
    time.sleep(3)

# Desloca para portão
    pyautogui.moveTo(1431,64)
    time.sleep(1)
    pyautogui.click(1431,64)
    time.sleep(4)
    pyautogui.moveTo(1337, 145)
    time.sleep(1)
    pyautogui.click(1337, 145)
    time.sleep(4)
    pyautogui.moveTo(1470, 151)
    time.sleep(1)
    pyautogui.click(1470, 151)
    time.sleep(4)
    pyautogui.moveTo(102, 227)
    time.sleep(1)
    pyautogui.click(102, 227)
    time.sleep(4)
    pyautogui.moveTo(307, 282)
    time.sleep(1)
    pyautogui.click(307, 282)
    time.sleep(4)

# Seleciona e Quebra portão
    pyautogui.moveTo(433, 169)
    time.sleep(1)
    pyautogui.click(433, 169)
    time.sleep(2)
    for i in range(2):
        skill1()
        skill2()
        skill3()
        skill4()
        time.sleep(2.5)

# Desloca para o centro da arena
    pyautogui.moveTo(65,226)
    time.sleep(1)
    pyautogui.click(65,226)
    time.sleep(4)
    pyautogui.moveTo(448, 362)
    time.sleep(1)
    pyautogui.click(448, 362)

# Manter ataque
    ataque = True
    while ataque == True:
        pegar()
        try:
            ok = pyautogui.locateOnScreen('ok.png', confidence=0.9)
            time.sleep(1)
            ok = pyautogui.center(ok) # Aqui dá o except
            okx, oky = ok
            for i in range(10):
                pegar()
                time.sleep(1)
            pyautogui.click(okx, oky)
            ataque = False
        except:
            pegar()
            buff1()
            pegar()
            target()
            skill1()
            target()
            pegar()
            skill2()
            target()
            pegar()
            skill3()
            pegar()
            target()
            skill4()
            pegar()
            target()
            pegar()

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