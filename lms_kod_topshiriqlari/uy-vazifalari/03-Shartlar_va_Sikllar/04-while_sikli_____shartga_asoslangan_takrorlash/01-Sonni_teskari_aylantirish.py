n = int(input())
if n == 0:
    print(0)
else:
    reversed_num = 0
    while n >     0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
print(reversed_num)