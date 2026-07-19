elements = input().split()
k = int(input())
result = elements[-k:]
print(*result)