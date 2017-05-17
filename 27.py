#Peças defeituosas
#Uma empresa produz 500 peças por dia. Dessas peças, são retiradas 5 pra realizar testes de qualidade.
#Os resultados dos testes podem ser 0 ou 1 para cada peça analisada. Se 3 peças ou mais obtiverem
#resultado 1, ou seja, são defeituosas, as peças produzidas naquele dia devem ser descartadas. Faça um
#algoritmo que receba os resultados das peças e determine se as peças vão ser descartadas ou não. A
#saída deve ser True ou False. Exemplo ==> Entrada: 0 0 1 1 1 / Saída: True

tool_state = input().split()
size = len(tool_state)
c = 0
a = 0

while c < size:
    if int(tool_state[c]) == 0:
        c = c + 1
    else:
        a = a + 1
        c = c + 1

if a >= 3 :
    print('True')
else:
    print('False')

