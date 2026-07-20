n = int(input())
groups = [input().split() for _ in range(n)]
print(max(groups, key=len)[0])