"""Programa para verificar e imprimir o maior elemento percorrendo duas listas. 
A função zip faz com que pare de percorrer o for assim que a menor lista acabar(for toda varrida).
Então a percorrerá a lista list_a toda e b percorrerá a list_b toda in zip(list_a, list_b) e o for será interrompido 
até que list_a seja totalmente varrida"""

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Adicione seu codigo aqui!
    if a > b:
        print a
    else:
        print b
    
    