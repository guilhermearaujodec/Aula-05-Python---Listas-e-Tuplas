# 8. Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba: 
# a) a quantidade de números pares contidos na lista 
# b) o somatório de todos os números ímpares contidos na lista.

# lista com 10 numeros pelo usuario
lista = []
for i in range(10):
    n = int(input("Digite um numero: "))
    lista.append(n)
print(lista)

# numeros pares da lista
contapares = 0
for item in lista:
    if item % 2 == 0:
        contapares += 1
print(f'Quantidade de pares: {contapares}')

# numero de impares da lista
contaimpares = 0
for item in lista:
    if item % 2 != 0:
        contaimpares +-1
print(f'Quantidade de impares {contaimpares}')

