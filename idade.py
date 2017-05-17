ages = input().split()
size = int(len(ages))
c = 0
soma = 0

while c < size - 1:
    soma = soma + int(ages[c])
    c = c + 1

media = soma / (size - 1)

print(media)