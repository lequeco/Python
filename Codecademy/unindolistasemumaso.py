"""Crie uma função chamada flatten que toma uma única lista e concatena todas as sublistas 
que são parte dela em uma única lista."""


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for numbers in lists: #numbers percorre lists
        for e in numbers: #e percorre numbers já que há listas dentro de listas
            results.append(e) #e é incrementado em results, ou seja, todos os elementos encontrados serão colocados em results
    return results #por fim results se torna uma lista só com elementos de várias listas separadas e por fim retornado

print flatten(n)