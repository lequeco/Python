import sys
def leitura():
    while True:
        try:
            cadeia = str(raw_input('Digite a cadeia do automato: '))
            for e in cadeia:
                if e not in [ 'a', 'b', 'c' ]:
                    print("A Cadeia nao contem os caracteres 'a', 'b' ou 'c'.") 
                    raise ValueError
            if cadeia[0] != 'a':
                print("A Cadeia nao inicia com 'a'.")
                raise ValueError                   
            break
        except(ValueError):
            print(cadeia, "Caracteres nao aceito na linguagem, Tente novamente")
    return cadeia
    

def caminho_superior():
    e=0 
    while cadeia[e] == 'a':
        pilha.append('C')
        pilha.append('C')
        e+=1       
    while cadeia[e] == 'b':
        pilha.pop(len(pilha)-1)       
        e+=1
        try:
            if e<len(cadeia) and len(pilha)==1: #N�o pertence pq a pilha n�o ta zerada
                print('A cadeia n�o pertence a linguagem: ') 
                entrada = int(raw_input('Se voc� deseja inserir uma nova cadeia digite 1, se n�o, digite 0: '))
                if entrada == 1:
                    return verifica
                if entrada == 0:
                    print('Programa encerrado: ')
                    x = int(input())
                    sys.exit()
        except ValueError:
            print('ERRO ')
        try:
            if len(pilha)==1:
                pilha.pop(0)
        except ValueError:
            print('ERRO ')
        try:
            if len(pilha)== 0: #Pertence pq a pilha se torna vazia desempilhando seu �ltimo conte�do
                print('A cadeia pertence a linguagem: ') 
                entrada = int(raw_input('Se voc� deseja inserir uma nova cadeia digite 1, se n�o, digite 0: '))
                if entrada == 1:
                    return verifica
                if entrada == 0:
                    print('Programa encerrado: ')
                    x = int(input())
                    sys.exit()
        except ValueError:
            print('ERRO ')
        try:
            if e>len(cadeia)-1: #A pilha n�o est� vazia e o contador j� superou o n�mero de opera��es
                print('A cadeia n�o pertence a linguagem: ')
                entrada = int(raw_input('Se voc� deseja inserir uma nova cadeia digite 1, se n�o, digite 0: '))
                if entrada == 1:
                    return verifica
                if entrada == 0:
                    print('Programa encerrado: ')
                    x = int(input())
                    sys.exit()
        except ValueError:
            print('ERRO ')
        try:
            if cadeia[e]=='a': #Se for encontrado um 'a' depois que for digitado um 'b' a cadeia n�o pertence
                print('A cadeia n�o pertence a linguagem: ')
                entrada = int(raw_input('Se voc� deseja inserir uma nova cadeia digite 1, se n�o, digite 0: '))
                if entrada == 1:
                    return verifica
                if entrada == 0:
                    print('Programa encerrado: ')
                    x = int(input())
                    sys.exit()
        except ValueError:
            print('ERRO ')


def caminho_inferior():
    e=0
    while cadeia[e] == 'a':
        e+=1
        pilha.append('C')
    while cadeia[e] == 'c':
        pilha.pop(len(pilha)-1)     
        e+=1

        try:
            if e<len(cadeia) and len(pilha)==1: #N�o pertence pq a pilha n�o ta zerada
                print('A cadeia n�o pertence a linguagem: ') 
                entrada = int(raw_input('Se voc� deseja inserir uma nova cadeia digite 1, se n�o, digite 0: '))
                if entrada == 1:
                    return verifica
                if entrada == 0:
                    print('Programa encerrado: ')
                    x = int(input())
                    sys.exit()
        except ValueError:
            print('ERRO ')
        try:
            if len(pilha)==1:
                pilha.pop(0)
        except ValueError:
            print('ERRO ')
        try:
            if len(pilha)== 0: #Pertence pq a pilha se torna vazia desempilhando seu �ltimo conte�do
                print('A cadeia pertence a linguagem: ')
                entrada = int(raw_input('Se voc� deseja inserir uma nova cadeia digite 1, se n�o, digite 0: '))
                if entrada == 1:
                    return verifica
                if entrada == 0:
                    print('Programa encerrado: ')
                    x = int(input())
                    sys.exit()
        except ValueError:
            print('ERRO ')
        try:
            if e>len(cadeia)-1: #A pilha n�o est� vazia e o contador j� superou o n�mero de opera��es
                print('A cadeia n�o pertence a linguagem: ') 
                entrada = int(raw_input('Se voc� deseja inserir uma nova cadeia digite 1, se n�o, digite 0: '))
                if entrada == 1:
                    return verifica
                if entrada == 0:
                    print('Programa encerrado: ')
                    x = int(input())
                    sys.exit()
        except ValueError:
            print('ERRO ')
    try:
        if len(pilha)!=0: #Se passar por todas as condi��es e no final a pilha n�o estiver vazia a cadeia n�o pertence a linguagem: casos como cadeias com ac ele encontre um b
            print('A cadeia n�o pertence a linguagem: ')
    except ValueError:
            print('ERRO ')



verifica = 1
encerra = 0
while verifica == 1:
    pilha = []
    cadeia = leitura()
    pilha = ['Z']
    e=0
    if 'b' in cadeia:
            caminho_superior()
    if 'c' in cadeia:
            caminho_inferior()


    







