#Total de Pessoas
#Escreva um algoritmo que receba a idade de várias pessoas. O algoritmo deve imprimir: O total de
##pessoas com menos de 21 anos e o total de pessoas com mais de 50 anos. Exemplo ==> Entrada: 2 5
#20 35 50 51 / Saída: 3 1
ages = input().split()
size = len(ages)
c = 0
below_21 = 0
above_50 = 0
while c < size:
    if int(ages[c]) < 21:
        below_21 = below_21 + 1
        c = c + 1

    else:
        c = c + 1
c = 0
while c < size:
    if int(ages[c]) > 50:
        above_50 = above_50 + 1
        c = c + 1
    else:
        c = c + 1

print(below_21,above_50)
