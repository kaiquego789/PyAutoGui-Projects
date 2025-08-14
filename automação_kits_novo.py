import pyautogui as pug
import pyperclip as pc
import time

pug.PAUSE = 0.25
pug.FailSafeException = True



while True:
    try:
        pug.alert('rodando o script')
        time.sleep(5)
        break
    except:
        ...
item = ""
item2 = ""
sku = ""
proximo = True

def atalho_sys():
    pug.hotkey('win', '5')

def atalho_excel():
    pug.hotkey('win', '7')

def pesquisa():
    atalho_excel()
    pug.click(x=1437, y=267, duration=0.15)
    pug.hotkey('ctrl', 'c')
    sku = pc.paste()
    atalho_sys()
    pug.click(x=350, y=66, duration=0.15)
    pug.click(x=462, y=536, duration=0.1)
    pug.write('igual')
    pug.click(x=505, y=533)
    pug.write(sku)
    pug.click(x=592, y=662, duration=0.1)

def msg_erro():
    global proximo
    pug.hotkey('ctrl', 'c')
    erro = pc.paste()
    if 'Nenhum' in erro:
        pug.press('enter')
        pug.click(x=754, y=421, duration=0.1)
        proximo = False
    else:
        proximo = True
        pug.press('enter')

def rolar_tela():
    pug.click(x=1908, y=978, duration=0.1)        

def obt_dados():
    pug.click(x=120, y=533, duration= 0.15, clicks=2)
    pug.hotkey('ctrl', 'c')
    item = pc.paste()
    atalho_excel()
    pug.click(x=1170, y=1000, duration=0.1)
    pug.click(x=1112, y=270, duration=0.1)
    pug.write(item)
    atalho_sys()
    pug.click(x=878, y=776, duration=0.1)
    pug.click(x=120, y=533, duration= 0.15, clicks=2)
    pug.hotkey('ctrl', 'c')
    item2 = pc.paste()
    while True:
        if item2 != item:
            print(item)    
            print(item2)
            atalho_excel()
            pug.press('tab')
            pug.write(item2)
            atalho_sys()
            pug.click(x=878, y=776, duration=0.1)
            pug.click(x=120, y=533, duration= 0.15, clicks=2)
            pug.hotkey('ctrl', 'c')
            item = item2
            item2 = pc.paste()
            continue
        else:
            atalho_excel()
            rolar_tela()
            pug.click(x=1102, y=1000, duration=0.1)
            rolar_tela()
            atalho_sys()
            break

while True:
    pug.PAUSE = 0.25
    pesquisa()
    msg_erro()
    if proximo is True:
        obt_dados()
        continue
    else:
        pug.PAUSE = 0.5
        atalho_excel()
        rolar_tela()
        pug.click(x=1176, y=1000, duration=0.1)
        rolar_tela()
        pug.click(x=1102, y=1000, duration=0.1)
        print(proximo)
        atalho_sys()
        continue