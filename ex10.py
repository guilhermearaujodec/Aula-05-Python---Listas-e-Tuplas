# 10. Preencha duas listas, uma para armazenar os nomes e outra para armazenar as idades de 
# pessoas. A entrada de dados deve ser finalizada quando o usuário informar um nome vazio. 
# Na sequência informe o nome de todas as pessoas que possuem idade igual ou superior a 
# 18 anos.

nomes = []
idades = []

while True:
    nome = input('Nome: ')
    if nome == '':
        break
    idade = int(input('Idade: '))
    nomes.append(nome)
    idades.append(idade)
    
for i in range(len(idades)):
    if idades[i] >= 18:
        print(nomes[i], idades[i])