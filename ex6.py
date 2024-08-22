# 6. Escreva uma função que remova todos os espaços em branco de uma string e retorne a string resultante. 

def lista_palavras(frase: str) -> str:
    """A função recebe a frase e remove os espaços"""
    
    lista = frase.replace(' ', '')                        # Separa os termos
    return lista

frase = input('Digite o texto: ').strip()
print(f'{lista_palavras(frase)}')