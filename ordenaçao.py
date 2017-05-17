#Ordenação
#Considere o programa para determinar se uma sequência de n números digitados pelo usuário está
#ordenado na forma crescente ou não. Faça o programa usando uma variável contadora. O programa
#deve imprimir "yes" ou "no". Exemplo ==> Entrada = 1 3 2 / Saída: no
numbers = input().split()
size = int(len(numbers))
c = 0
menor = 0
maior = 0
verification = 1
while c < size - 1:
    menor = int(numbers[c])
    maior = int(numbers[c + 1])
    c = c + 1
    if maior > menor:
        verification = verification + 1

if verification == size:
    print("yes")
else:
    print("no")