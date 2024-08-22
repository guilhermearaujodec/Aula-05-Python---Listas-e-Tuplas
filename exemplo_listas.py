# LISTAS
# Estruturas de dados que armazena um conjunto de itens

# itens são separados por vírgula e delimitados por colchetes [ ]
lista = [5, 10, 30, 40]
print(lista)

# listas são heterogêneas (armazenam dados de tipos diferentes)
lista = [3, 'abc', 2.555, 'asasa', 23]

# listas são mutáveis (podem ser modificadas)
lista = [5, 10, 30, 40]
lista[0] = 100

# alterando o valor da posição zero para 100
print(lista)

#percorrer os itens da lista somente
lista = [5,6,10,30,7]
cont = 0
for item in lista:
    if item %2 --0:
        cont +=1
    print(item)
    


#percorrer os indices da lista e alterar
cont = 0
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
    print(lista[i])
    

# len - retorna o tamanho da lista !!!!
lista = [4, 60, 2, 5, 10]
print(len(lista))

# append - insere um item no final da lista
lista = [4, 60, 2, 5, 10]
lista.append(100)
print(lista)

# insert - insere um item em um indice específico dal lista
lista.insert(0, 200)
print(lista)

# pop - remove o último item da lista
lista.pop()
print(lista)

# pop(indice) - remove o item de um indice
lista.pop(0)
print(lista)

# remove - remove um item da lista de acordo com o valor indicado (remove somente o primeiro item localizado)
lista = [3, 200, 40, 6, 200, 6, 200, 200]
lista.remove(200)
print(lista)

# remove todas as ocorrencias de um item da lista
while 200 in lista:
    lista.remove(200)
print(lista)

# count - conta a quantidade de vezes que um item ocorre na lista
lista = [2, 5, 6, 7, 6, 10, 6]
print(lista.count(6))
print(lista.count(50))

# index - retorna o indice da primeira ocorrência de um item
lista = [2, 5, 6, 7, 6, 10, 6]
print(lista.index(6))

valor = int(input('Digite um número: '))
if valor in lista:
    print(lista.index(valor))
else:
    print('O valor não está na lista')

# exibe todos os índices onde um item se encontra
print('------------------------')    
lista = [3, 200, 5, 200, 5, 6, 7, 200]
for i in range(len(lista)):
    if lista[i] == 200:
        print(i)
        
# sort - ordena uma lista em ordem crescente
lista = [3, 200, 5, 200, 5, 6, 7, 200]
lista.sort()
print(lista)

lista = ['maçã', 'laranja', 'Abacaxi', 'abc', 'teste']
lista.sort()
print(lista)

# sorted - retorna uma cópia da lista ordenada
lista = [4, 8, 1, 3, 19, 2]
listaordenada = sorted(lista)
print(listaordenada)

# min - menor item da lista
lista = [4, 8, 1, 3, 19, 2]
print(min(lista))

# max = maior item da lista
lista = [4, 8, 1, 3, 19, 2]
print(max(lista))

# sum - somatória de uma lista
lista = [4, 8, 1, 3, 19, 2]
print(sum(lista))

# media dos itens da lista
media = (sum(lista)) / len(lista)
print(media)

# preencher uma lista com entradas do usuário
lista = []
for i in range(5):                          # cinco itens
    n = int(input('Número: '))
    lista.append(n)
print(lista)

lista = []
while True:                                 # quantidade inderteminada (até digitar zero)
    n = int(input('Número: '))
    if n == 0:
        break
    lista.append(n)
print(lista)
    
