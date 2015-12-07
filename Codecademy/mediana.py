#Função que calcula a mediana de uma lista de números
def median(numbers):
    mediana = sorted(numbers)
    m = 0

    if(len(numbers)+1) % 2 == 0:
        m = mediana[((len(numbers)) / 2)]
        return m
    else:
        pos1 = len(numbers) / 2
        pos2 = (len(numbers) / 2) - 1
        m = (mediana[pos1] + mediana[pos2]) / (2.0)
        return m
   
print median([1, 1, 2])
print median([7, 3, 1, 4])