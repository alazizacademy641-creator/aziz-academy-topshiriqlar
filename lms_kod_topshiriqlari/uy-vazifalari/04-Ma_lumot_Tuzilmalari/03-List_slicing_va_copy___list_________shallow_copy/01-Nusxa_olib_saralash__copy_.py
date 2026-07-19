nums = list(map(int, input().split()))
num_copy = nums[:]
num_copy.sort()
print(*nums)
print(*num_copy)