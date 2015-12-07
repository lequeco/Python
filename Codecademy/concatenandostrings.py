n = ["Michael", "Lieberman"]

def join_strings(words): #Função que concatena 2 strings aplicando for 
    result = ""
    for e in range(0, len(words)): #para cada elemento e num alcance de 0-tamanho da lista word faça
        result = result + words[e] # reuslt = result + cada letra presente na lista word
    return result

print join_strings(n)