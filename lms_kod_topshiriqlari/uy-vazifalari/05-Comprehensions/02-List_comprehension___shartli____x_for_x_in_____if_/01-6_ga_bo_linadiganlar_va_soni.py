nums = [int(x) for x in input().split()]

res = [x for x in nums if x % 2 == 0 and x % 3 == 0]

print(res)
print(len(res))