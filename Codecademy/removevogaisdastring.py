#Função que tira as vogais de uma string

def anti_vowel(text):
    new_text = ""
    for e in range(len(text)):
        if text[e].lower() != 'a' and \
        text[e].lower() != 'e' and \
        text[e].lower() != 'i' and \
        text[e].lower() != 'o' and \
        text[e].lower() != 'u':
            new_text += text[e]
    return new_text