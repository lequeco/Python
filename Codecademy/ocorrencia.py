#Função que verifica o numero de ocorrencias de um elemento dentro de uma lista

def count(sequence, item):
    ocorrence = 0
    for e in sequence:
        if e == item:
            ocorrence += 1
    return ocorrence
    
print count([1, 3, 5, 3, 9], 3)