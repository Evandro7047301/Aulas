import random

def matriz(x,y):
    matriz = []
    x = input("linhas:")
    y = input("colunas:")
    for i in range(x):
        linha = []
        for j in range(y):
            valor = int(input("~ "))
            linha.append(valor)
        matriz.append(linha)
    return matriz



def imprimir(matriz):
    for i in matriz:
        print(i)
def media(matriz):
    media = []
    for i in range(0,3):
        c = i
        for g in range(0,i):
            media.append(matriz[c][g])
    soma = 0
    for x in media:
        soma += x
    resultado = soma/len(media)
    return resultado

a = media(matriz(4,4))
print(a)