n = int(input())
factorial = 1
counter = 1

while counter <= n:
    factorial *= counter
    counter += 1
print(factorial)