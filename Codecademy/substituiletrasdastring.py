#Função que recebe duas strings e poe * no lugar das palavras de uma delas, sendo que uma está dentro da outra.
#Funciona sem acentos ou letras maiúsculas

def censor(text, word):
   text = text.split(word) #Split faz com que tudo que seja word, no caso, casa, seja separado em text
   new = "*" * len(word) #New faz com que o caractere asterísco "*" seja multiplicado o tamanho de vezes da string word
   text = new.join(text) #Text então será a união de new em text, ou seja, vamos unir todos os * em text
   return text
   
print censor("esta casa eh uma semi-casa", "casa")