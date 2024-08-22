# 5. Implemente uma função que retorne a quantidade de palavras existentes em uma string.

def conta_palavras(frase: str) -> list:
    """A função recebe a frase e conta as palavras"""
    
    lista = frase.split(' ')                        # Separa os termos
    return len(lista)

frase = input('Digite o texto: ').strip()
print(f'{conta_palavras(frase)}')