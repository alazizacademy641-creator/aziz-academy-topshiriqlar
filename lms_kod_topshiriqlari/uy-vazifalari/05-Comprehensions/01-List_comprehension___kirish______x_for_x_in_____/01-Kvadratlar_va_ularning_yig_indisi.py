nums = list(map(int, input().split()))

kvadratlar = [x * x for x in nums]
print(kvadratlar)

print(sum(kvadratlar))