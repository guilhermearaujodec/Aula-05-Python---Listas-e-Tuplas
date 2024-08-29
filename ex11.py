# 11. Preencha  duas  tuplas  com  5  números  cada,  informados  pelo  usuário.  Concatene  as  duas 
# tuplas e exiba a tupla resultante. 
 
# Exemplo: Suponha que as tuplas contenham os números: 
# (3, 1, 5, 3, 5) 
# (5, 5, 7, 3, 1). 
# Como resultado, o programa deve gerar a tupla: 
# (3, 1, 5, 3, 5, 5, 5, 7, 3, 1). 


lista1 = []
for i in range(5):
    n = int(input('Numero: '))
    lista1.append(n)
    
lista2 = []
for i in range(5):
    n = int(input('Numero: '))
    lista2.append(n)
    
tupla1 = tuple(lista1)
tupla2 = tuple(lista2)
tupla3 = tupla1 + tupla2
print(tupla1)
print(tupla2)    
print(tupla3)    