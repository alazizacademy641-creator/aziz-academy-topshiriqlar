n = int(input())
toq_sonlar = []
for _ in range(n):
    x = int(input())
    if x % 2 != 0:
        toq_sonlar.append(x)
toq_sonlar.sort()

print(*toq_sonlar)