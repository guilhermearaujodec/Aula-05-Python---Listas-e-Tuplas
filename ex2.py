# 2. Crie  uma  função  que  receba  uma  string  e  retorne  a  mesma  string  com  todas  as  letras  em maiúsculas. 

def uppercase(frase: str) -> str:
    """Retorna a frase com todas as letras em maiúsculo"""
    return frase.upper()

frase = input('Digite a frase: ')

print(f'A sua frase ficou assim: "{uppercase(frase)}"')