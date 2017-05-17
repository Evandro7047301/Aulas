#Número primo é um número inteiro que admite exatamente 4 divisores. O conceito sobre números primos para inteiros englo
#ba tanto números positivos como negativos. Os únicos divisores de 3 são {-3, -1, 1, 3}. O número 3 é primo.
number = int(input())
c = 1
verification = 0
if number > 0:
    while c <= number:
        if number % c == 0:
            verification = verification + 1
            c = c + 1
        else:
            c = c + 1
c = -1
if number < 0:
    while c >= number:
        if number % c == 0:
            verification = verification + 1
            c = c - 1
        else:
            c = c - 1

if verification == 2:
    print("yes")
else:
    print("no")