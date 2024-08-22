# TUPLA
# Sequencia de itens delimitada por parênteses
# estrutura imutável - não pode ser modificada
tupla = (3, 6, 2, 10, 30)
print(tupla)
print(tupla[0])

for item in tupla:
    print(item)
    
# tupla vazia
tupla = ()
print(tupla)

# tupla com 1 único elemento
tupla = (10,)     # Somente nas tuplas de único elemento precisa-se colocar uma ',' no final
print(tupla)

tupla = (3, 6, 2, 10, 30)
print(max(tupla))
print(min(tupla))
print(sum(tupla))
print(len(tupla))

print(tupla.count(6))
print(tupla.index(6))

ufs = ['AC', 'SP', 'RJ', ]

coordenadas = [(23.555, 10.888), (45.4989, 34.989)]
print(coordenadas[0][1])                    # printa apenas o 10.888

coordenadas [0] = 3
print(coordenadas)

tupla = ([3, 5, 6], [1, 2, 3])
tupla[0][0] = 999
print(tupla)

# list - converte uma tupla para lista
tupla = (4, 5, 6)
lista = list(tupla)
print(lista)

# tuple - converte uma lista para tupla
lista = [4, 7, 10]
tupla = tuple(lista)
print(tupla)

# como modificar ordenar os dados
tupla = (4, 1, 70, 3, 2)
lista = list(tupla)
lista . sort()
tupla = tuple(lista)
print(tupla)