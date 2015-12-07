numbers = [3, 5, 7]

def total_de_elementos(numbers): #Função que conta quantos elementos possui uma lista
    result = 0
    for e in numbers:
    #for e in range(len(numbers)):
        result = result + 1
    return result

def total_da_soma_de_elementos(numbers): #Função que soma os elementos presentes numa lista [0] + [1] + [2] ...
    result = 0
    for e in range(len(numbers)):
    #for e in numbers:	
        result = result + numbers[e]
    return result


print total_de_elementos(numbers) #result = 3
print total_da_soma_de_elementos(numbers) #result = 15