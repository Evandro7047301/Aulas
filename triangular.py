number = int(input())
multiplier = 1

while (multiplier + 1) * (multiplier) * (multiplier + 2) < number:
    multiplier = multiplier + 1

if (multiplier + 1) * (multiplier) * (multiplier + 2) == number:
    print("True")
else:
    print("False")