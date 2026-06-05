n = int(input())
total  = 0
i = 1
while i <= n:
    if i % 9 == 0:
        i += 1
        continue
    total += i 
    i += 1
print(total)