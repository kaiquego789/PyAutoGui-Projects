import pyautogui as pug
import time
import pyperclip as pc
pug.FailSafeException=True
pug.PAUSE = 0.2

qntd_repet = int(pug.prompt('Quantas repetições de nota fazer de uma só vez?'))
qntd_feita = 0
n_de_produtos = int(pug.prompt('Quantos produtos voce quer na nota?'))
nc_de_produtos = 0
cliente_id = str(pug.prompt('Qual o ID do cliente?'))
pug.alert('Colocar a seleção do Excel na coluna A1')
fen = int(pug.prompt('Qual o fen da operação?'))
test = 0
print(test)
n_nf = 0
data_nf = 0

def atalho_excel():
    with pug.hold('win'):
        pug.press('7')

def atalho_sys():
    with pug.hold('win'):
        pug.press('5')

def cliente():
    pug.write(cliente_id)
    pug.press('Enter', interval=0.1)
    pug.press('Enter', interval=0.1)    
    pug.press('Enter', interval=0.1)
    pug.press('Enter', interval=0.1)

def produtos():
    atalho_excel()
    time.sleep(0.5)
    pug.press('Enter') #sempre deixar a seleção na coluna A1
    pug.hotkey('ctrl', 'c')
    atalho_sys()
    pug.hotkey('ctrl', 'v')
    pug.press('Enter', interval=0.1)

def tabela():
    atalho_excel()
    pug.hotkey('tab')
    pug.hotkey('ctrl', 'c')
    atalho_sys()
    pug.hotkey('ctrl', 'v')
    pug.press('Enter', interval=0.1)
    pug.press('Enter', interval=0.1)
    pug.press('Enter', interval=0.1)

def quantidade():
    pug.press('Enter', interval=0.1)
    pug.press('Enter', interval=0.1)
    pug.press('Enter', interval=0.1)
    atalho_excel()
    pug.hotkey('tab')
    time.sleep(0.1)
    pug.hotkey('ctrl', 'c')
    atalho_sys()
    time.sleep(0.2)
    pug.hotkey('ctrl','v')
    pug.press('Enter', interval=0.1)
    pug.press('Enter', interval=0.1)
    atalho_excel()
    pug.press('Enter', interval=0.1)
    atalho_sys()
    pug.click(x=347, y=504, duration=0.2)
    
def nota_nova():
    pug.hotkey('ctrl', 'n', interval=0.2)
    pug.write(str(fen))
    pug.press('Enter', interval=0.15)
    pug.press('Enter', interval=0.15)
    cliente()

def transportadora():
    pug.press("Enter", presses=4, interval=0.15)
    pug.write("1")

def obs():
    pug.click(x=1040, y=803, duration=0.2)
    pug.press('Backspace', presses=50, interval=0.1)
    pug.write("BAIXA PERCA QUEBRA CONFORME ARTIGO 125, S 8O, DO RICMS/2000. ITENS DA DANF DE ORIGEM IMPORTACAO NO. ", interval=0.2)
    pug.write(n_nf, interval=0.05)
    pug.press('Backspace', interval=0.05)
    pug.write(" DIA ")
    pug.write(data_nf, interval=0.1)
    pug.press('Backspace', interval=0.1)

def obs_venda():
    pug.click(x=1040, y=803, duration=0.2)
    pug.press('Backspace', presses=50, interval=0.1)
    pug.write("MERCADORIA DESTINADA A REVENDA", interval=0.2)
    
def fechar_numero_transmitir():
    pug.hotkey('ctrl', 'g', interval=0.1)
    time.sleep(2)
    pug.click(x=840, y=410, duration=0.1)
    time.sleep(1)
    #pug.press('Enter', interval=0.1)
    while True:
        pug.hotkey('ctrl', 'c')
        msg = pc.paste()
        if 'Deseja' in msg:
            pug.press('Enter')
            time.sleep(0.5)
            break
        time.sleep(0.5)
        continue
    time.sleep(1.2)
    pug.press('Enter')
    while True:
        pug.hotkey('ctrl', 'c')
        msg = pc.paste()
        if 'Confirme' in msg:
            pug.press('Enter')
            time.sleep(0.5)
            break
        time.sleep(0.5)
        continue
    pug.press('Enter', interval=1, presses=2)
    time.sleep(0.5)    
    pug.click(x=1015, y=410, duration=0.1)
    time.sleep(3)
    pug.press('Enter', interval=0.1)
    while True:
        pug.hotkey('ctrl', 'c')
        msg = pc.paste()
        if 'email' in msg:
            pug.press('right', interval=0.1)
            pug.press('Enter', interval=0.1)
            pug.click(x=1020, y=360, duration=0.2)
            break
        time.sleep(0.5)
        continue    
def n_nota_n_data():
    global n_nf, data_nf
    pug.press('tab', interval=0.2)
    pug.hotkey('ctrl', 'c') #numero da nota
    n_nf = pc.paste()
    pug.press('tab', interval=0.2)
    pug.hotkey('ctrl', 'c') #data da nota xx/xx/xxxx
    data_nf = pc.paste()
    time.sleep(0.1)
    pug.press('Enter', interval=0.1)
    time.sleep(0.1)
    atalho_sys()
    time.sleep(1)


if (test == 1):
    while(qntd_feita!=qntd_repet):
        atalho_sys()
        transportadora()
        if(fen == 20):
            atalho_excel()
            n_nota_n_data()
            obs()
            fechar_numero_transmitir()
        qntd_feita +=1
        nc_de_produtos = 0

if (test == 0):
    while(qntd_feita!=qntd_repet):
        atalho_excel()
        time.sleep(0.1)
        atalho_sys()
        time.sleep(0.1)
        nota_nova()
        while(nc_de_produtos!=n_de_produtos):
            produtos()
            time.sleep(0.5)
            tabela()
            time.sleep(0.5)
            quantidade()
            nc_de_produtos +=1
        transportadora()
        if(fen == 20):
            atalho_excel()
            n_nota_n_data()
            obs()
            fechar_numero_transmitir()
            qntd_feita +=1
            nc_de_produtos = 0
        if(fen == 1 or fen == 1):
            atalho_excel()
            n_nota_n_data()
            obs_venda()
            fechar_numero_transmitir()
            qntd_feita +=1
            nc_de_produtos = 0     

if (test == 2):
    pug.alert('Selecionar a linha A1')
    while(qntd_feita!=qntd_repet):
        atalho_excel()
        pug.press('tab', interval=0.15)
        pug.hotkey('ctrl', 'c', interval=0.2)
        with pug.hold('win'):
            pug.press('0')
        time.sleep(0.5)
        pug.click(x=350, y=70, duration=0.2)
        pug.click(x=657, y=489, duration=0.2)
        pug.hotkey('ctrl', 'v', interval=0.15)
        pug.click(x=757, y=660, duration=0.2)
        pug.press('Enter', interval=0.15)
        pug.click(x=1015, y=406, duration=0.2)
        time.sleep(3)
        pug.click(x=469, y=744, duration=0.5)
        time.sleep(3)
        pug.press('Enter', interval=0.15)
        time.sleep(7)
        pug.press('Enter', interval=0.15)
        pug.click(x=1025, y=360, duration=0.2)
pug.alert('Finalizado')