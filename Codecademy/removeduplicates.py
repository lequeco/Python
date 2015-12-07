#Função que remove itens iguais numa lista

def remove_duplicates(lista):
    new = []
    for e in lista:
        if e not in new:
                new.append(e)
    return new
    
print remove_duplicates([1, 3, 4, 4, 6, 4]) 