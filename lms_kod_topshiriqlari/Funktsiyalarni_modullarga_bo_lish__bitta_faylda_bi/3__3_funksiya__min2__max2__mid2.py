a, b = map(int, input().split())

def min2(x, y):
    return min(x, y)

def max2(x, y):
    return max(x, y)

def mid2(x, y):
    return (x + y) / 2 

print(min2(a, b))
print(max2(a, b))
print(f"{mid2(a, b):.2f}")