import time
import pyautogui
import BuffAndSkill as bk

# Entra dg se tiver entrada
pyautogui.moveTo(980, 610)
time.sleep(1)
pyautogui.click(980, 610)
# Não quero q fique entrando
# se não houver entrada, tenho que consertar.
time.sleep(5)

# Inicia dg
inicia = pyautogui.locateOnScreen('inicia.png', confidence=0.9)
inicia = pyautogui.center(inicia)
iniciax, iniciay = inicia
pyautogui.click(iniciax, iniciay)
time.sleep(3)

# Locomove dentro da dg
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
    bk.skill1()
    bk.skill2()
    bk.skill3()
    bk.skill4()
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
    bk.pegar()
    try:
        ok = pyautogui.locateOnScreen('ok.png', confidence=0.9)
        time.sleep(1)
        ok = pyautogui.center(ok) # Aqui dá o except
        okx, oky = ok
        for i in range(10):
            bk.pegar()
            time.sleep(1)
            pyautogui.click(okx, oky)
            ataque = False
    except:
        bk.pegar()
        bk.buff1()
        bk.pegar()
        bk.target()
        bk.skill1()
        bk.target()
        bk.pegar()
        bk.skill2()
        bk.target()
        bk.pegar()
        bk.skill3()
        bk.pegar()
        bk.target()
        bk.skill4()
        bk.pegar()
        bk.target()
        bk.pegar()