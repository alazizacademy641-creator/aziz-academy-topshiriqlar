import math
n = int(input())

if n <= 1:
    print("yo'q")
else:
    is_prime = True
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            is_prime= False
            break
    if is_prime:
        print("ha")
    else:
        print("yo'q")