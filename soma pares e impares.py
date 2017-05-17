#Somas Pares e Ímpares
#Faça um programa que leia vários inteiros positivos e mostre, no final, a soma dos números pares e a
#soma dos números ímpares, nessa ordem. A entrada termina com o numero -1. Exemplo ==> Entrada =
#5 1 2 2 4 -1 / Saída = 8 6
numbers = input().split()
size = int(len(numbers))
c = 0
soma_impar = 0
soma_par = 0
while c < size - 1:
    if int(numbers[c]) % 2 == 0:
        soma_par = soma_par + int(numbers[c])
        c = c + 1
    else:
        c = c + 1
c = 0
while c < size - 1:
    if int(numbers[c]) % 2 != 0:
        soma_impar = soma_impar + int(numbers[c])
        c = c + 1
    else:
        c = c + 1
print(soma_par, soma_impar)
