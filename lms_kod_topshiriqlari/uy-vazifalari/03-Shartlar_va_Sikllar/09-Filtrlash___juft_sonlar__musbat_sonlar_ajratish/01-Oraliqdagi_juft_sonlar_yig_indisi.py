a = int(input())
b = int(input())
yigindi = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        yigindi += i
print(yigindi)