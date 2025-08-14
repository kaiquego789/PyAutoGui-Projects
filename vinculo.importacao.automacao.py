import pyautogui as pug
import pyperclip as pc
import time

pug.PAUSE = 0.5
pug.FAILSAFE = True

quantidade_a_fazer = 0
fazer = int(pug.prompt('Quantos Produtos serão inclusos?'))
pug.alert('Iniciando a automação, pressione OK para prosseguir.')
sku = ''

def atalho_excel():
    pug.hotkey('win', '7')

def atalho_sys():
    pug.hotkey('win', '5')

def checagem():
    pug.click(x=188, y=777, duration=0.2)
    time.sleep(1)
    while True:
        pug.hotkey('ctrl', 'c')
        msg = pc.paste()
        if 'agora' in msg:
            pug.press('Enter')
            break
        time.sleep(0.25)
    while True:
        pug.hotkey('ctrl', 'c')
        msg = pc.paste()
        if 'Base' in msg:
            pug.press('right')
            pug.press('enter')
            break 
        time.sleep(0.25)           
    while True:
        pug.hotkey('ctrl', 'c')
        msg = pc.paste()
        if 'ajuda' in msg:
            pug.press('Enter')
            break
        time.sleep(0.25)        

checagem()
while quantidade_a_fazer != fazer:
    pug.click(x=914, y=451, duration=0.2, clicks=2)
    pug.hotkey('ctrl', 'c')
    item_vinculado = pc.paste()
    if " " in item_vinculado: #Sequecia para fazer o vinculo
        pug.click(x=175, y=452, duration=0.2, clicks=2)
        pug.hotkey('ctrl', 'c')
        atalho_excel()
        pug.click(x=1350, y=243, duration=0.2)
        pug.hotkey('ctrl', 'shift', 'v')
        pug.press('tab')
        pug.hotkey('ctrl', 'c')
        pug.click(x=1450, y=264, duration=0.2)
        pug.hotkey('ctrl', 'shift', 'v')
        pug.hotkey('ctrl', 'c')
        sku = pc.paste()
        if 'AND' in sku or 'and' in sku:
            atalho_sys()
            pug.click(x=1100, y=452, duration=0.2)
            pug.click(x=618, y=749, duration=0.2)
            pug.click(x=624, y=547, duration=0.2)
            pug.write("Igual")
            pug.click(x=651, y=545, duration=0.2)
            pug.write(sku)
            pug.click(x=760, y=648, duration=0.2)
            time.sleep(2)
            pug.hotkey('ctrl', 'c')
            msg = pc.paste()
            if "Nenhum registro recuperado" in msg:
                pug.press('enter')
                pug.click(x=917, y=410, duration=0.2)
                pug.click(x=1130, y=751, duration=0.2)
                quantidade_a_fazer += 1
                continue
            else:
                pug.press('Enter', interval=0.5, presses=3)
                time.sleep(2.5)
                pug.hotkey('ctrl', 'c')
                msg = pc.paste()
                if 'confirma' in msg:
                    pug.press('Enter')
                    quantidade_a_fazer += 1
                    continue
                else:
                    pug.press('Enter')
                    pug.click(x=917, y=452, duration=0.2)
                    pug.click(x=1130, y=693, duration=0.2)
                    quantidade_a_fazer += 1
                    continue
    else:
        quantidade_a_fazer += 1
        continue            
pug.alert('Vinculos finalizados, verifique possiveis lacunas!')