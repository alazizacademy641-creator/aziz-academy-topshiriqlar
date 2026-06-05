def squares(n):
    result = []
    for i in range(1, n + 1):
        result.append(i ** 2)
    return result 

n = int(input())
res  = squares(n)
print(*res)