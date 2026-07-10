A = set(map(int, input().split()))
B = set(map(int, input().split()))

umumiy = A.intersection(B)

farqi = A.difference(B)

print(*(sorted(umumiy)))
print(*(sorted(farqi)))