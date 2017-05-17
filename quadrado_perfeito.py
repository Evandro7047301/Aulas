#Quadrado Perfeito
#Escreva um algoritmo que receba vários números e verifique se eles são ou não quadrados perfeitos.
#Um número é quadrado perfeito quando tem um número inteiro como raiz quadrada. A saída deve ser a
#quantidade de quadrados perfeitos. Exemplo ==> Entrada: 2 4 9 4 16 / Saída: 4

numbers = input().split()
size = int(len(numbers))
c = 0
c2 = 0
result = 0
while c < size:
    verification = int(numbers[c]) ** (1/2)
    number_verification = str(verification)
    size_2 = len(number_verification)
    while c2 < size_2:
        if number_verification[c2] == '.':
            c2 = c2 + 1
            if int(number_verification[c2]) == 0:
                result = result + 1
        else:
            c2 = c2 + 1
    c = c + 1
    c2 = 0

print(result)