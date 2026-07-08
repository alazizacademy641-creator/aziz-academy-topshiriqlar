words = input().split()

result = [w for w in words if w[0] in "aeiou"]

print(result)