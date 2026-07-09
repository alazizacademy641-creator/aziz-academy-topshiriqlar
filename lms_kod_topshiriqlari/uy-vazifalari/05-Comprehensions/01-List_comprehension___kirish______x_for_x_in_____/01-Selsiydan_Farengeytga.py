nums = (map(int, input().split()))

result = [c * 9 // 5 + 32 for c in nums]

print(result)