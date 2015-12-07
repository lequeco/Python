#Função para reverter uma string e retorná-la ao contrário

word = "weslley"

def reverse(text):
    reverso = ""
    tam = len(text) - 1
    for e in text:
        count = text[tam]
        reverso += count
        tam -= 1
    return reverso  
    
print reverse(word)