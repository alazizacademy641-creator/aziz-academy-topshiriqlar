n = int(input())
yigindi = 0

while n > 0:
    yigindi += n % 10
    n //= 10
print(yigindi)