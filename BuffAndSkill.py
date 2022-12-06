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