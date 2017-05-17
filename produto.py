#Produto
#Faça um programa que calcula o produto dos números digitados pelo usuário. A entrada termina com o
#valor zero. Exemplo ==> Entrada = 1 5 7 0 / Saída = 35
numbers = input().split()
size = int(len(numbers))
c = 0
produto = 1

while c < size - 1:
    produto = produto  * int(numbers[c])
    c = c + 1

print(produto)