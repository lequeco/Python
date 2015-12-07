#Função para verificar se o número é primo ou não

def is_prime(x):
    if x == 2 or x == 3:
        return True
    elif x == 1 or x <= 0:
        return False
    for n in range(2, x):
        P = int(n)
        if x % P == 0:
            return False
    else:
        return True