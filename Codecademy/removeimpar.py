#Função que retira os números ímpares de uma lista e retorna os números pares

def purify(numbers):
    pares = []
    for e in numbers:
        if e % 2 == 0:
            pares += [e]
    return pares
    
print purify([1, 2, 3, 4, 5, 6])