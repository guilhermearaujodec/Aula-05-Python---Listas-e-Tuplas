# 3. Crie uma função que retorne a quantidade de vogais (a, e, i, o, u) existentes em uma string.

def cont_vogais(frase: str) -> int:
    """A função conta a quantidade de vogais dentro da string"""
    
    vogais = 'aeiou'
    cont = 0
    
    for caracter in frase:
        if caracter.lower in vogais:
            cont += 1
    return cont
    
frase = input('Digite o texto: ')
print(cont_vogais(frase))

