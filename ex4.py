# 4. Escreva um programa que receba uma frase como entrada e retorne uma lista das palavras presentes na frase.

def lista_palavras(frase: str) -> list:
    """A função recebe a frase e separa as palavras"""
    
    lista = frase.split(' ')                        # Separa os termos
    return lista

frase = input('Digite o texto: ').strip()
print(f'{lista_palavras(frase)}')