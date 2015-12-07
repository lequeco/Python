"""Função que soma os elementos de um numero inteiro passados como parametro para uma função"""

x = 1234

def digit_sum(n):
    count = 0 #inicializo um cotador
    n = str(n) #transformo o número em uma string
    for e in n: #percorro a string fazendo com que para cada elemento da string:
        e = int(e) #este elemento se torne um inteiro
        count = count + e #atualizo count sendo ele + o elemento percorrido, por exemplo, 1 depois 2 depois 3 depois 4
    return count #retorno count
        
print digit_sum(x) #imprimo a função passando o numero 1234 como parâmetro. A saída é 10       
