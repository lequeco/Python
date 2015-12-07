"""Função para calcular o fatorial de um número"""

def factorial(x): #A função factorial recebe o número que será "Fatoriado"
    fac = x
    if fac == 0 or fac == 1:
        print("O fatorial deste numero tem valor 1")
        return 0
      #Crio uma variável fac que receberá este número
    while x != 1: #Crio um lanço while que entrará em loop até que x seja diferente de 1, Quando x for igual a 1 ele para
        fac = fac * (x - 1) #fac receberá a operação do fac atual * o valor de x - 1, por exemplo. fac = 4 * 3
        x -= 1 #Enquanto tudo isso ocorre x será decrementado
    return fac #Quando x for igual a 1 o while acaba e o resultado final de fac será retornado
    
y = int(input("Digite um numero para calcular seu fatorial: "))
print(factorial(y))
