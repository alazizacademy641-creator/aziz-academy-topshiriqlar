sanog = 0
while (n := int(input())) != 0:
    if n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
        sanog += 1
print(sanog)