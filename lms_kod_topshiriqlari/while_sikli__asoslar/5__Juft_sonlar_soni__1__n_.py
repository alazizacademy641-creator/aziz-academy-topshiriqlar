n = int(input())
counter = 1
count = 0
while counter <= n:
    if counter % 2 == 0:
        count += 1
    counter += 1
print(count)