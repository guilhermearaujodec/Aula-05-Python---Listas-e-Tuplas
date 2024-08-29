# 9. Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista 
# com os números pares e outra com os números ímpares.  
# Exemplo:  
# Suponha que os números digitados são: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8].  
# Para esta lista, o programa deve gerar as seguintes listas: 
# [4, 8, 8] 
# [1, 7, 9, 5, 3, 7, 9]


lista = []
for i in range(10):
    n = int(input('Número: '))
    lista.append(n)
print(lista)

pares = []
impares = []
for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print(pares)
print(impares)