# 1. Escreva uma função que receba uma string e retorne o número de caracteres nela.

def conta_caraceteres(frase: str) -> int:
    """Retorna a quantidade de caracteres de uma string."""
    return len(frase)

frase = input('Digite a frase: ')
quantidade = conta_caraceteres(frase)
print(quantidade)