nums = list(map(int,(input().split())))

result = [x * x for x in nums if x % 3 == 0]

print(result)