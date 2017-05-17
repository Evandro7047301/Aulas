linhas = 8
colunas = 11
matriz = []
alien = []
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

while '' == '':
    print('')
    matriz[2][10] = 'x'
    matriz[2][0] = 'x'
    matriz[3][0] = 'x'
    matriz[3][10]  = 'x'
    matriz[5][10] = '-'
    matriz[5][0] = '-'
    matriz[6][10] = '-'
    matriz[6][0] = '-'
    matriz[7][1] = 'x'
    matriz[7][3] = '-'
    matriz[7][4] = '-'
    matriz[7][9] = 'x'
    matriz[7][7] = '-'
    matriz[7][6] = '-'

    while c < linhas:
        for x in range(11):
            print(matriz[c][x],end=' ')
        print('')
        c += 1
    c = 0
    print('')
   

    matriz[2][10] = '-'
    matriz[2][0] = '-'
    matriz[3][0] = '-'
    matriz[3][10]  = '-'
    matriz[5][10] = 'x'
    matriz[5][0] = 'x'
    matriz[6][10] = 'x'
    matriz[6][0] = 'x'
    matriz[7][1] = '-'
    matriz[7][3] = 'x'
    matriz[7][4] = 'x'
    matriz[7][9] = '-'
    matriz[7][7] = 'x'
    matriz[7][6] = 'x'

    while c < linhas:
        for x in range(11):
            print(matriz[c][x],end=' ')
        print('')
        c += 1
    c = 0




