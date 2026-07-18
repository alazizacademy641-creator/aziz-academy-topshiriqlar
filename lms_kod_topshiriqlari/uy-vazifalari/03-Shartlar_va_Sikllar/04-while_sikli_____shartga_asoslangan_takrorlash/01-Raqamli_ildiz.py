n = int(input())
while n >= 10:
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    n = sum_digits
print(n)