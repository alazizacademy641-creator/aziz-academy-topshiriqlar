words = input().split()
res = [w for w in words if len(w) >= 5]
print(res)