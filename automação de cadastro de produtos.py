import pyautogui as pug
import time
import pyperclip as pc

while True:
    try:
        pug.FailSafeException=True
        pug.PAUSE = 0.225
        n_cad_prod = int(pug.prompt('Com quantos produtos você vai trabalhar?'))
        n_prod_cad = 0
        tempo = 27
        tipo_operacao = int(pug.prompt('Qual tipo de operação você quer fazer?'))
        menssagem = ""
        qntd_acerto = 0
        sku1 = ""
        copia = ""
        dados = True
        break
    except:
        pug.alert('Você digitou Valores inválidos')
        sair = pug.prompt('Deseja refazer?')
        if sair == 'Sim' or sair == 'sim' or sair == 'S' or sair == 's':
            continue
        else:
            dados = False
            break

"""
DEFEININDO AS FUNÇÕES DA AUTOMAÇÃO
"""

def atalho_excel():
    with pug.hold('win'):
        pug.press('7')
def atalho_sys():
    with pug.hold('win'):
        pug.press('5')
def n_original():
    pug.hotkey('ctrl', 'n', interval=0.15)
    pug.click(x=370, y=400, duration=0.1, clicks=3)
    atalho_excel()
    pug.click(x=1383, y=270, duration=0.1)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    pug.hotkey('ctrl','v', interval=0.15)
def referencia():
    atalho_excel()
    pug.click(x=1480, y=270, duration=0.1)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    pug.click(x=370, y=420, duration=0.1)
    pug.hotkey('ctrl','v', interval=0.15)
def produto():
    atalho_excel()
    pug.click(x=1570, y=270, duration=0.1)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    pug.click(x=370, y=450, duration=0.1)
    pug.hotkey('ctrl','v', interval=0.15)
def fabricante():
    atalho_excel()
    pug.click(x=1650, y=270, duration=0.2)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    pug.doubleClick(x=370, y=515, duration=0.2)
    pug.hotkey('ctrl','v', interval=0.15)
def gp_fiscal():
    atalho_excel()
    pug.click(x=1730, y=270, duration=0.2)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    pug.doubleClick(x=370, y=530, duration=0.2)
    pug.hotkey('ctrl','v', interval=0.15)
    pug.press('enter', interval=0.15) #confirmando o grupo fiscal
    pug.press('enter', interval=0.15)
def estoque_preco():
    pug.click(x=580, y=330, duration=0.2)
def operacionais():
    pug.click(x=500, y=330, duration=0.2)
def oem():
    atalho_excel()
    pug.click(x=1886, y=270, duration=0.2)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    pug.click(x=380, y=680, duration=0.2, clicks=3)
    pug.hotkey('ctrl','v', interval=0.15)
def preco():
    atalho_excel()
    pug.click(x=1965, y=270, duration=0.2)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    time.sleep(0.1)
    pug.tripleClick(x=550, y=560)
    time.sleep(0.1)
    pug.hotkey('ctrl','v', interval=0.15)
def ipi():
    atalho_excel()
    pug.click(x=2060, y=270, duration=0.2)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    time.sleep(0.1)
    pug.tripleClick(x=860, y=530)
    time.sleep(0.1)
    pug.hotkey('ctrl','v', interval=0.15)
def Vnd_Vista1():
    atalho_excel()
    pug.click(x=2144, y=270, duration=0.2)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    pug.tripleClick(x=360, y=700, duration=0.2)
    pug.hotkey('ctrl','v', interval=0.15)
    pug.press('enter', interval=0.2)
def salvamento():
    pug.hotkey('ctrl','g', interval=0.2)
    pug.press('enter',interval=0.2)
    pug.hotkey('ctrl','g', interval=0.2)
    pug.press('enter',interval=0.2)
    time.sleep(tempo)
    pug.press('enter', interval=0.2)
def rolar_tela():
    atalho_excel()
    pug.click(x=2548, y=980, duration=0.2)
    atalho_sys()
def pesquisar_sku():
    atalho_excel()
    pug.click(x=1480, y=270, duration=0.2)
    pug.hotkey('ctrl','c', interval=0.15)
    atalho_sys()
    pug.click(x=350, y=70, duration=0.2)
    pug.click(x=626, y=561, duration=0.4)
    pug.write("igual", interval=0.09)
    pug.click(x=695, y=558, duration=0.2)
    pug.hotkey('ctrl','v', interval=0.15)
    pug.click(x=764, y=655, duration=0.2)
    pug.press('enter', interval=0.15)
    time.sleep(0.5)
    pug.press('enter', interval=0.15)
def abrindo_excel():
    pug.click(x=1364, y=1056, duration=0.05)    
def salvamento_sem_sinc():
    pug.hotkey('ctrl','g', interval=0.05)
    pug.press('right',interval=0.2)
    pug.press('enter',interval=0.05)
def faltam():
    a = n_cad_prod - n_prod_cad
    print("Faltam", a, "para serem cadastrados:")
def acerto():
    pug.click(x=971, y=431, duration=0.2)
    atalho_excel()
    pug.click(x=2280, y=270, duration=0.2)
    pug.hotkey('ctrl','c', interval=0.15)
    qntd_acerto = int(pc.paste())
    if(int(qntd_acerto)<0): #subtração
        #pug.tripleClick(x=671, y=583, duration=0.2)
        pug.click(x=2380, y=270, duration=0.2)
        pug.hotkey('ctrl','c', interval=0.15)
        atalho_sys()
        pug.hotkey('ctrl','v', interval=0.15)
        pug.tripleClick(x=607, y=613, duration=0.2)
        pc.copy(str(menssagem))
        pug.hotkey('ctrl','v', interval=0.15)
        pug.click(x=811, y=585, duration=0.2)
    elif(int(qntd_acerto)>0): #adição
        #pug.tripleClick(x=671, y=583, duration=0.2)
        pug.click(x=2380, y=270, duration=0.2)
        pug.hotkey('ctrl','c', interval=0.15)
        atalho_sys()
        pug.hotkey('ctrl','v', interval=0.15)
        pug.tripleClick(x=607, y=613, duration=0.2)
        pc.copy(str(menssagem))
        pug.hotkey('ctrl','v', interval=0.15)
        pug.click(x=811, y=555, duration=0.2)
        pug.click(x=870, y=645, duration=0.1)
    else:
        pug.click(x=870, y=645, duration=0.1)
def basico():
    pug.click(x=250, y=330)
def salvar_fornecedor():
    pug.hotkey('ctrl', 'e', interval=0.2)
    time.sleep(0.25)
    pug.press('Enter', interval=0.15)
    pug.click(x=370, y=400, duration=0.2, clicks=3)
    pug.hotkey('ctrl','c', interval=0.15)
    pug.click(x=650, y=332)
    pug.click(x=612, y=488, duration=0.1)
    time.sleep(0.15)
    pug.press('enter', interval=0.15)
    pug.hotkey('ctrl','v', interval=0.15)
def ult_compras():
    pug.click(x=905, y=333, duration=0.2)
    pug.doubleClick(x=755, y=400, interval=0.15)
    pug.hotkey('ctrl', 'c', interval=0.15)
    copia = pc.paste()
    if(sku1 != copia):
        atalho_excel()
        pug.press('tab', presses=2, interval=0.2)
        pug.hotkey('ctrl', 'v', interval=0.15)
        atalho_sys()
        pug.doubleClick(x=631, y=400, interval=0.15)
        pug.hotkey('ctrl', 'c', interval=0.15)
        atalho_excel()
        pug.press('tab', interval=0.2)
        pug.hotkey('ctrl', 'v', interval=0.15)
        atalho_sys()
        pug.tripleClick(x=300, y=400, interval=0.15)
        pug.hotkey('ctrl', 'c', interval=0.15)
        atalho_excel()
        pug.press('tab', interval=0.2)
        pug.hotkey('ctrl', 'v', interval=0.15)
        atalho_sys()
    if(sku1 == copia):
        atalho_excel()
        pug.press('Enter', interval=0.15)
        atalho_sys()    

if dados:
    if tipo_operacao == 1: #criando um novo cadastro
        atalho_sys()
        while(n_prod_cad!=n_cad_prod):
            pug.click(x=27, y=72, duration=0.2)
            n_original()
            referencia()
            produto()       
            fabricante()
            gp_fiscal()
            estoque_preco()
            preco()
            ipi()
            Vnd_Vista1()
            operacionais()
            oem()
            salvamento()
            rolar_tela()
            n_prod_cad += 1
            faltam()
        pug.alert("Cadastros finalizados")

    if tipo_operacao == 2: #editando Oem
        pug.click(x=1275, y=1060, duration=0.2)
        while(n_prod_cad!=n_cad_prod):
            abrindo_excel()
            pesquisar_sku()
            operacionais()
            oem()
            salvamento_sem_sinc()
            rolar_tela()
            n_prod_cad += 1
            faltam()
            pug.alert("OEM(s) editados")

    if tipo_operacao == 3: #editando o preço
        pug.click(x=1275, y=1060, duration=0.2)
        while(n_prod_cad!=n_cad_prod):
            
            abrindo_excel()
            pesquisar_sku()
            estoque_preco()
            preco()
            #ipi()
            Vnd_Vista1()
            salvamento_sem_sinc()
            rolar_tela()
            n_prod_cad += 1
            faltam()
        pug.alert("Custos editados")    

    if tipo_operacao == 4: #testador de variaveis
        print("Numero de produtos a serem cadastrados:", n_cad_prod)
        print("Numero de produtos cadastrados:",n_prod_cad)
        print("Tempo:", tempo)
        print("Tipo da operação:", tipo_operacao)
        print("Texto copiado:", qntd_acerto, type(qntd_acerto))

    if tipo_operacao == 5: #edição de fornecedor e acerto de estoque
        alt_custo = pug.prompt('Vai alterar o custo da planilha?')
        menssagem = str('Acerto nf de importacao')
        while(n_prod_cad!=n_cad_prod):
            pesquisar_sku()
            basico()
            salvar_fornecedor()
            basico()
            n_original()
            fabricante()
            if(alt_custo=="Sim" or alt_custo=="sim" or alt_custo=="S" or alt_custo=="s"):
                estoque_preco()
                preco()
                #ipi()
                Vnd_Vista1()
            operacionais()
            oem()
            salvamento_sem_sinc()
            rolar_tela()
            n_prod_cad +=1
        
        pug.alert("forncedores e quantidades alterados")

    if tipo_operacao == 6: #pegar valor/nf/data de importação de determinado produto
        pug.alert('Selecionar B1')
        pug.PAUSE = 0.18
        while(n_prod_cad!=n_cad_prod):
            atalho_excel()
            pug.press('Enter', interval=0.1)
            pug.hotkey('ctrl', 'c', interval=0.1)
            sku1 = pc.paste()
            atalho_sys()
            pug.click(x=350, y=70, duration=0.15)
            pug.click(x=626, y=561, duration=0.2)
            pug.write("igual")
            pug.click(x=695, y=558, duration=0.2)
            pug.hotkey('ctrl','v', interval=0.15)
            pug.click(x=764, y=655, duration=0.2)
            pug.press('Enter', interval=0.2)
            pug.press('Enter', interval=0.2)
            ult_compras()
            n_prod_cad +=1
        pug.alert('Dados copiados')

    if tipo_operacao == 7: #Somente acerto de estoque
        menssagem = pug.prompt(str('Observação do acerto:'))
        pug.alert('Verifique a selecao.')
        while (n_prod_cad!=n_cad_prod):
            pesquisar_sku()
            estoque_preco()
            acerto()
            rolar_tela()
            n_prod_cad +=1
        pug.alert('Acertos finalizados!')    
