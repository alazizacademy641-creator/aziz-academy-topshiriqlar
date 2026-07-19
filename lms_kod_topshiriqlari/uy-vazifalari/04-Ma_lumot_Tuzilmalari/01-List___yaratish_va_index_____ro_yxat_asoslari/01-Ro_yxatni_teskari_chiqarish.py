nums = input().split()
result = []
for i in range(len(nums) - 1, -1, -1):
    result.append(nums[i])
print(*result)