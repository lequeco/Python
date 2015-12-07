#Função que calcula o produto dos números presentes em uma lista

def product(numbers):
    produtos_numbers = 1
    for e in numbers:
        produtos_numbers = produtos_numbers * e
    return produtos_numbers
    
print product([2, 4, 6])