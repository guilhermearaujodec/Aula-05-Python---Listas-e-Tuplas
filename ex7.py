# 7. Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba: 
# a) o maior número da lista 
# b) o menor número da lista 
# c) a média dos números contidos na lista

def numeros_inteiros() -> None:
    """
    A função solicita para que o usuário insira alguns números inteiros e exiba:
    
    a) o maior número da lista 
    b) o menor número da lista 
    c) a média dos números contidos na lista
    """
    
    
    for n in range (10):
        lista  = []
        lista = lista.append(int(input('Insira um número: ')))
    print(lista)
    
    print(f'Maior: {max(lista)}')
    print(f'Menor: {min(lista)}')
    print(f'Média: {sum(lista) / len(lista)}')
          
print(f'{numeros_inteiros()}')