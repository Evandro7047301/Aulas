linhas = 8
colunas = 11
matriz = []
alien = []
backup = matriz[:]
c = 0
alien.append('--x-----x--')
alien.append('---x---x---')
alien.append('--xxxxxxx--')
alien.append('-xx-xxx-xx-')
alien.append('xxxxxxxxxxx')
alien.append('x-xxxxxxx-x')
alien.append('x-x-----x-x')
alien.append('---xx-xx---')


while c < linhas:
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(alien[c][j])
        matriz.append(linha)
        c += 1

c = 0
while c < linhas:
    for x in range(11):
        print(matriz[c][x],end=' ')
    print('')
    c += 1
c = 0

for x in range():
    matriz[0][x] = matriz [x][0]