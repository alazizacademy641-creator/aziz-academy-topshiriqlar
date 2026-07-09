nums = list(map(int, input().split()))

result = [x for x in nums if x % 2 == 0]

print(result)