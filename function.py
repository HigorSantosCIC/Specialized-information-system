from pyke import knowledge_engine as ke 
from pyke import contexts
import os

sus = ke.engine(__file__)
sus.activate('regras')
sus.get_kb('relacao')
## Contador das doenças: dengue, zika e chiku
global_cont_dengue = 0
global_cont_zika = 0 
global_cont_chiku = 0

## Febre
def febre():
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Com respeito aos sintomas:")
    print("Qual o grau, e duração da febre:")
    print("1- Acima de 38ºC (4 a 7 dias)")
    print("2- Sem febre ou subfebril 38ºC (1-2 dias subfebril)")
    print("3- Febre alta maior que 38ºC (2-3 dias)")
    febre = int(input())
    while(febre <= 0 or febre > 3):
        print("Insira uma opção válida (1 - 3): ")
        febre = int(input())

    #Adiciona ao contador e relaciona a prova da biblioteca pyke
    
    if febre == 1:
        ans, _ = sus.prove_1_goal('relacao.febre(1, $sick)')
        global_cont_dengue += 1
    
    elif febre == 2:
        ans, _ = sus.prove_1_goal('relacao.febre(2, $sick)')
        global_cont_zika+=1

    elif febre == 3:
        ans, _ = sus.prove_1_goal('relacao.febre(3, $sick)')
        global_cont_chiku+=1

print("\n" * os.get_terminal_size().lines)

## Manchas na pele
def mancha():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Insira o intervalo de tempo mais próximo das aparições de manchas na pele")
    print("1- A partir do 1º ou 2º dia")
    print("2- A partir do 2º ao 5º dia")
    print("3- A partir do 4º dia")
    mancha = int(input())
    while(mancha <= 0 or mancha > 3):
        print("Insira uma opção válida (1 - 3): ")
        mancha = int(input())

    if mancha == 1:
        ans, _ = sus.prove_1_goal('relacao.mancha(2, $sick)')
        ans, _ = sus.prove_1_goal('relacao.mancha(3, $sick)')
        global_cont_zika+= 0.90
        global_cont_chiku+= 0.10

    elif mancha == 2:
        ans, _ = sus.prove_1_goal('relacao.mancha(3, $sick)')
        global_cont_chiku+= 0.50
    
    elif mancha == 3:
        ans, _ = sus.prove_1_goal('relacao.mancha(1, $sick)')
        ans, _ = sus.prove_1_goal('relacao.mancha(3, $sick)')
        global_cont_dengue+= 0.40
        global_cont_chiku += 0.50



## Nível de dor nos musculos
def dor_musc():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Insira o nível de dor nos musculos")
    print("1- Dor Leve")
    print("2- Dor Leve / Moderada")
    print("3- Dor Moderada / Intensa")
    dor_musc = int(input())
    while dor_musc <= 0 or dor_musc > 3:
        print("Insira uma opção válida (1 - 3): ")
        dor_musc = int(input())

    if dor_musc == 1:
        ans, _ = sus.prove_1_goal('relacao.dor_musc(3, $sick)')
        global_cont_chiku += 1
    
    elif dor_musc == 2:
        ans, _ = sus.prove_1_goal('relacao.dor_musc(2, $sick)')
        global_cont_zika += 1
    
    elif dor_musc == 3:
        ans, _ = sus.prove_1_goal('relacao.dor_musc(1, $sick)')
        global_cont_dengue += 1
        
## Dor nas articulações
def dor_art():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Insira a frequência da dor articular")
    print("1- Leve")
    print("2- Dor Leve / Moderada")
    print("3- Dor Moderada / Intensa")
    dor_art = int(input())
    while dor_art <= 0 or dor_art > 3:
        print("Insira uma opção válida (1 - 3): ")
        dor_art = int(input())

    if dor_art == 1:
        ans, _ = sus.prove_1_goal('relacao.dor_art(1, $sick)')
        global_cont_dengue += 1
    
    elif dor_art == 2:
        ans, _ = sus.prove_1_goal('relacao.dor_art(2, $sick)')
        global_cont_zika += 1

    elif dor_art == 3:
        ans, _ = sus.prove_1_goal('relacao.dor_art(3, $sick)')
        global_cont_chiku += 1

## Intensidade da dor articular
def intens_art():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Insira a intensidade da dor articular")
    print("1- Leve")
    print("2- Leve / Moderada")
    print("3- Moderada / Intensa")
    intens_art = int(input())
    while intens_art <= 0 or intens_art > 3:
        print("Insira uma opção válida (1 - 3): ")
        intens_art = int(input())
    
    if intens_art == 1:
        ans, _ = sus.prove_1_goal('relacao.dor_art(1, $sick)')
        global_cont_dengue += 1
    
    elif intens_art == 2:
        ans, _ = sus.prove_1_goal('relacao.intens_art(2, $sick)')
        global_cont_zika += 1

    elif intens_art == 3:
        ans, _ = sus.prove_1_goal('relacao.intens_art(3, $sick)')
        global_cont_chiku += 1

## Ederma 
def edema_articulacao():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku

    print("Insira presenca de edema da articulacao: ")
    print("1- Nao possui")
    print("2- Possui, de leve intensidade")
    print("3- Possui, de moderada a elevada intensidade")

    edema = int(input())

    while(edema <= 0 or edema > 3):
    	print("Insira uma opcao valida (1 - 3): ")
    	edema = input()
    
    if edema == '1':
    	ans, _ = sus.prove_1_goal('relacao.edema(1, $sick)')
    	global_cont_dengue+= 1

    if edema == "2":
    	ans, _ = sus.prove_1_goal('relacao.edema(2, $sick)')
    	global_cont_zika+= 1
    
    if edema == "3":
    	ans, _ = sus.prove_1_goal('relacao.edema(3, $sick)')
    	global_cont_chiku+= 1

## Conjuntivite 
def conjuntivite():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Insira a presença de conjuntivite")
    print("1- Possui")
    print("2- Não possui")
    conjuntivite = int(input())
    while conjuntivite <= 0 or conjuntivite > 2:
        print("Insira uma opção válida (1 ou 2): ")
        conjuntivite = int(input())
    if conjuntivite == 1:
        ans, _ = sus.prove_1_goal('relacao.conjuntivite(2, $sick)')
        ans, _ = sus.prove_1_goal('relacao.conjuntivite(3, $sick)')
        global_cont_zika += 0.90
        global_cont_chiku += 0.30
    
    elif conjuntivite == 2:
        ans, _ = sus.prove_1_goal('relacao.conjuntivite(1, $sick)')
        global_cont_dengue += 1
        

## Dor de cabeça
def dor_cabeca():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Presença de dor de cabeça")
    print("1 - Leve")
    print("2 - Moderado")
    print("3 - Intenso")
    dor_cabeca = int(input())
    while dor_cabeca <= 0 or dor_cabeca > 3:
        print("Insira uma opção válida (1 - 3): ")
        dor_cabeca = int(input())
    if dor_cabeca == 1:
        pass
    if dor_cabeca == 2:
        ans, _ = sus.prove_1_goal('relacao.dor_cabeca(2, $sick)')
        ans, _ = sus.prove_1_goal('relacao.dor_cabeca(3, $sick)')
        global_cont_chiku += 1
        global_cont_zika += 1

    elif dor_cabeca == 3:
        ans, _ = sus.prove_1_goal('relacao.dor_cabeca(1, $sick)')
        global_cont_dengue += 1


## Coceira
def coceira():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Presença de coceira")
    print("1 - Leve")
    print("2 - Moderada/Intensa")
    print("3 - Intensa")
    coceira = int(input())
    while coceira <= 0 or coceira > 3:
        print("Insira uma opção válida (1 - 3): ")
        coceira = int(input())
    if coceira == 1:
        ans, _ = sus.prove_1_goal('relacao.coceira(1, $sick)')
        ans, _ = sus.prove_1_goal('relacao.coceira(3, $sick)')
        global_cont_dengue += 1
        global_cont_chiku += 1
    
    elif coceira == 2:
        ans, _ = sus.prove_1_goal('relacao.coceira(2, $sick)')
        global_cont_zika += 1
    
    elif coceira == 3:
        ans, _ = sus.prove_1_goal('relacao.coceira(2, $sick)')
        global_cont_zika += 1

## Hipertrofia Ganglionar
def hiper_gang():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Frequência de Hipertrofia Ganglionar")
    print("1 - Leve")
    print("2 - Moderado")
    print("3 - Intenso")
    hiper_gang = int(input())
    while hiper_gang <= 0 or hiper_gang > 3:
        print("Insira uma opção válida (1 - 3): ")
        hiper_gang = int(input())

    if hiper_gang == 1:
        ans, _ = sus.prove_1_goal('relacao.hiper_gang(1, $sick)')
        global_cont_dengue += 1
    
    elif hiper_gang == 2:
        ans, _ = sus.prove_1_goal('relacao.hiper_gang(3, $sick)')
        global_cont_chiku += 1

    elif hiper_gang == 3:
        ans, _ = sus.prove_1_goal('relacao.hiper_gang(2, $sick)')
        global_cont_zika += 1
        

## Discrasia Hemorrágica
def disc_hemorr():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Frequência de Discrasia hemorrágica")
    print("1 - Não possui")
    print("2 - Leve")
    print("3 - Moderado")
    disc_hemorr = int(input())
    while disc_hemorr <= 0 or disc_hemorr > 3:
        print("Insira uma opção válida (1 - 3): ")
        disc_hemorr = int(input())

    if disc_hemorr == 1:
        ans, _ = sus.prove_1_goal('relacao.disc_hemorr(2, $sick)')
        global_cont_zika +=1
    
    elif disc_hemorr == 2:
        ans, _ = sus.prove_1_goal('relacao.disc_hemorr(3, $sick)')
        global_cont_chiku += 1
    
    elif disc_hemorr == 3:
        ans, _ = sus.prove_1_goal('relacao.disc_hemorr(1, $sick)')
        global_cont_dengue += 1
## Acometimento Neurológico

def neuro():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku
    print("Acometimento Neurológico")
    print("1 - Possui")
    print("2 - Não possui")
    neuro = int(input())
    while neuro <= 0 or neuro > 2:
        print("Insira uma opção válida (1 - 2): ")
        neuro = int(input())

    if neuro == 1:
        ans, _ = sus.prove_1_goal('relacao.neuro(2, $sick)')
        global_cont_zika += 1
    
    elif neuro == 2:
        ans, _ = sus.prove_1_goal('relacao.neuro(1, $sick)')
        ans, _ = sus.prove_1_goal('relacao.neuro(3, $sick)')
        global_cont_dengue += 1
        global_cont_chiku += 1

def result():
    print("\n" * os.get_terminal_size().lines)
    global global_cont_dengue 
    global global_cont_zika
    global global_cont_chiku

    total = global_cont_chiku + global_cont_dengue + global_cont_zika

    print("Diagnóstico para Dengue:" ,     round(((global_cont_dengue/total) * 100), 2) , "%")
    print("Diagnóstico para Zika:" ,       round(((global_cont_zika/total) * 100),   2) , "%")
    print("Diagnóstico para Chikungunya:", round(((global_cont_chiku/total) * 100),  2) , "%")

sus.reset()