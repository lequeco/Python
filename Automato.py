import sys #biblioteca usada simplesmente para utilizar sys.exit(), para encerrar o programa quando digitar 'e'

#Função para encontrar todas as posições em que o padrão ocorre no texto
def EncontraPadroesNoTexto(texto, padrao): 

	inicio = 0
	fim = len(texto) #fim recebe o tamanho do texto
	L = []
	I = []

	while(inicio != fim): #for e in range(0, fim): #para cada elemento de 0 até o tamanho do texto, ou seja se tamanho do texto for 16 o for vai de 0 até 15
		indice = texto.find(padrao, inicio, fim) #indice recebe a posicao em que o padrao ocorre no texto no intervalo início até fim
		if indice >= 0: #se o padrão for encontrado no texto, a variável indice recebe a posição que o padrão começa, se o padrão não existir no texto, indice recebe -1 pelo retorno da função find()
			L.append(indice) #adiciona o indice em que o padrão ocorre
		inicio = inicio + 1 #inicio = indice + len(padrao) - 1 #o novo início começa da posição do último caractere do padrão até o fim, pois se o padrão for aba e no texto existir ababa eu tenho que procurar mais padrões à partir de aba e n de ba
					
	for z in L:
		if z not in I:
			I.append(z)
   	
	return I #retorna a lista contendo todos os índices em que o padrão ocorre no texto. Como Flávio quer que o texto comece de 1, quando for imprimir o índice é só imprimir indice + 1

#Função para imprimir a tabela formada pelo padrão e o alfabeto.
def tabela_padrao(padrao, alfabeto, M):

	#Recebendo como parâmetro o padrão, a lista chamada de alfabeto contendo o alfabeto do padrão e a matriz já montada mais abaixo no código...
	print ('Tabela Delta:')

	#Para cada estado de 0 até tamanho do padrão + 1, ou seja de o padrão for 'abab', seu tamanho é 4 e a tabela vai de 0 até 4, então o for vai até 5 para que fique 0 1 2 3 4
	for estado in range(0, len(padrao) + 1):
		for x in alfabeto: #Para cada caractere deste alfabeto
			posicao_lendo = alfabeto.index(x) #posicao_lendo recebe o índice deste caractere na lista alfabeto, ou seja, se alfabeto for ['a', 'b'], o index de a é 0 e o de b é 1
			posicao_destino = M[estado][posicao_lendo] #posicao_destino será o valor da matriz M no estado estado lendo o caractere x M[estado][posicao_lendo]
			if(posicao_destino != 0): #se o resultado deste estado lendo o caractere não for para o estado 0, deve-se printar
				if(x == ' '):
					print("[%d, " % (estado) + "'%s']: " % (x) + "%d" % (posicao_destino))#Exemplo: [0, ' ']: 1		       	
				else:
					print("[%d, %s]: %d" % (estado, x, posicao_destino))#Exemplo: [0, a]: 1

#Função para imprimir a tabela formada pelo texto e o alfabeto. 
"""
def tabela_texto(texto, alfabeto, M):

	#Esta função só está aqui porque eu pensei que a tabela delta era a tabela do alfabeto no texto e o professor quer que seja a tabela do alfabeto no padrão
	print ('Tabela Delta:')

	#Funciona da mesma forma mas ao invés de eu estar na posição 0 1 2 3 ou 4 ou ... do padrão eu olho do texto e vejo que caractere do texto eu to lendo e praonde vai
	estado_anterior = 0
	estado_atual = 0

	for e in range(0, len(texto)):

		i = e + 1
		if(texto[e:i] in alfabeto):
			estado_anterior = estado_atual
			posicao = alfabeto.index(texto[e:i])
			estado_atual = M[estado_anterior][posicao]
			if(M[estado_anterior][posicao] != 0):
				if(texto[e:i] == ' '):
					print("[%d, " % (estado_anterior) + "'%s']: " % (texto[e:i]) + "%d" % (estado_atual))
				else:
					print("[%d, %s]: %d" % (estado_anterior, texto[e:i], estado_atual))
"""

#texto = str(raw_input()) -> python 2
#texto = str(input()) -> python 3

#O programa começa aqui e mais embaixo chama as funções que estão implementadas acima
tamanho_texto = int(input()) #variável para receber o tamanho do texto, não uso para nada, deixo aqui somente para não falhar nos casos de testes quando informa o tamanho do texto, já que em python não precisa declarar um vetor de char limitando seu tamanho.
texto = str(input()) #variável para receber o texto
padrao = str(input()) #variável para receber o padrao
operacao = str(input()) #variável para receber a operacao
alfabeto = [] #o alfabeto inicialmente é uma lista vazia
simbolos = ['.', ',', ' '] #essa lista chamada de simbolos é utilizada para organzizar a ordem de ponto, virgula e espaço como Flávio pediu

#Para preencher a lista com o alfabeto faz-se
for e in padrao: #Para cada elemento do padrão:
	if e not in alfabeto: #Se este elemento não está na lista...claramente não vai estar pois a lista está inicialmente vazia, e se ler um caractere repetido, ele já estará na lista
		alfabeto.append(e) #insira este elemento na lista

alfabeto = sorted(alfabeto) #ordena o alfabeto em ordem crescente tanto de inteiro quanto de caracter. a lista alfabeto recebe o retorna da função sorted nesta mesma lista alfabeto, ou seja, o alfabeto recebe ele mesmo agora ordenado
#print(alfabeto)

#Este processo organiza a questão da ordem de ponto, virgula e espaço como Flávio pediu. Como na tabela ascii ponto, vírgula e espaço tem valores 46, 44, 32 respectivamente eles ficam em ordem(mas não como Flávio pediu) após o sorted(), mas Flávio quer ao contŕario
for x in simbolos: #Então para cada elemento x na lista simbolos:
	if x in alfabeto: #se este elemento x existe na lista alfabeto
		alfabeto.remove(x) #retiro ele da lista alfabeto independente de qualquer posição que ele esteja
		alfabeto.append(x) #insiro ele novamente na lista alfabeto. Quando se utiliza a função append(elemento), este elemento é adicionado na lista na última posição.
#Ou seja, como a lista símbolos já é inicializada na ordem que Flávio quer, basta percorré-la verificando se algum elemento dela existe no alfabeto e remove e insere novamente ele no fim para que fique na ordem

#Aqui é criada uma 'Matriz' setadas com zeros do tamanho do padrão + 1. Digo 'Matriz' porque não existe Matriz em Python, existe lista encadeada, uma lista com listas dentro, que pode-se manipular em forma de matriz
M = [0] * (len(padrao) + 1)

#Então para cada linha dessa lista, eu crio mais uma lista do tamanho do alfabeto. Exemplo: se padrão = 'abab'. M = [0, 0, 0, 0, 0]
for i in range(0, len(padrao) + 1):
	M[i] = [0] * len(alfabeto) #ao fazer com que M[i] = [0] * alfabeto ['a', 'b'] com tamanho 2. M agora será igual á: M[ [0, 0], [0, 0], [0, 0], [0, 0]. [0, 0] ], uma matriz 5x2

#Aqui é montada a matriz de transição de estados, igual ao pseudocódigo que ele deu na sala. O(M³ * |E|)

tamanho_padrao = len(padrao)
for q in range(0, tamanho_padrao + 1): #Para cada elemento q de 0 até o tamanho do padrão + 1
	for x in alfabeto: #Para cada elemento x do alfabeto
		k = min(tamanho_padrao + 1, q + 2) #k recebe o menor valor entre min(tamanho_padrao + 1, q + 2)
		k = k - 1 
		z = 0
		if(q == len(padrao)): #Aqui é o caso comparar sufixo e prefixo quando a string já está no último estado
			z = z + 1	
		while(k != -1):
			#print ("valor de K: %d, Alfabeto: %s, Valor de Q: %d" % (k, x, q))
			string = padrao[z : q] + x
			if (string.startswith(padrao[0 : k]) == True): #verifica se o padrão no intervalo[0 : k] concatenado com o caractere x é prefixo do padrão no intervalo[z : q]. quando vc tem uma string e pede para imprimir string[0:1], ela é tratada como vetor, no caso em Python uma lista e vc pode verificar o valor dela neste intervalo, da posição 0 até a 1
				#print ("%s é prefixo de %s" % (padrao[0 : k], string))
				break #se for prefixo, significa que uma certa quantidade de elementos iguais uma string tem em relação a outra, e K terá este valor, se uma for 'ab' e a outra for 'ab', k = 2, então o estado será mudado para 2
			else:
				#print ("%s não é prefixo de %s" % (padrao[0 : k], string))
				k = k - 1
				z = z + 1
		M[q][alfabeto.index(x)] = k #A Matriz no estado q lendo o caractere x do alfabeto recebe o valor do estado que o automato irá.		
		#Nesta matriz esta questão de estar no estado tal e ler o caractere tal é tratado como, estado q lendo a posição do caractere x na lista alfabeto, por isto index(x). Exemplo abaixo.

#Tabela criada com padrão = 'abab' e alfabeto = ['a', 'b'].
"""
		 a   b
	______________	   
	0  | 1 | 0 | 
	1  | 1 | 2 | 
	2  | 3 | 0 |
	3  | 1 | 4 |
	4  | 3 | 0 |

	q = posicões(linhas) ou estados atuais do automato
	x = carctere lido em relação ao estado que está. 

	*quando q igual a 0...q lendo index(a) que seria na matriz M[0][0] vai pra 1, então a matriz M[0][0] = 1
	*quando q igual a 0...q lendo index(b) que seria na matriz M[0][1] vai pra 0, então a matriz M[0][1] = 0

	*quando q igual a 1...q lendo index(a) que seria na matriz M[1][0] vai pra 1, então a matriz M[1][0] = 1
	*quando q igual a 1...q lendo index(b) que seria na matriz M[1][1] vai pra 2, então a matriz M[1][1] = 2

	e assim sucessivamente

"""

while(operacao != 'e'):

	if operacao == 's': #quando a operação escolhida for 's', chama a função de encontrar os índices do padrão no texto
		lista = EncontraPadroesNoTexto(texto, padrao) #A Lista nomeada de lista recebe a lista retornada pela função EncontraPadroesNoTexto
		if lista: #se a lista não estiver vazia...
			for e in lista: #então ela possui elementos com índices >= 0 onde o padrão ocorre no texto. percorre essa lista
				print(e + 1) #imprime o índice do elemento da lista + 1 onde o padrão ocorre no texto

	if operacao == 'u': #quando a operação escolhida for 'u', chama a função de tabela delta do padrão
		tabela_padrao(padrao, alfabeto, M)

	#if operacao == 't': #quando a operação escolhida for 't', chama a função de tabela delta do texto(Não precisa para o trabalho eu fiz pq pensei que era ela e depois soube que era a do padrão)
		#tabela_texto(texto, alfabeto, M)

	if operacao == 'e': #quando a operação escolhida for 'e', chama a função sys.exit() que encerra o programa
		sys.exit()	

	operacao = str(input()) #faz escolher uma nova operação até que não se digite 'e'