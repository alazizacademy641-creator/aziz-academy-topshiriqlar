a, b = map(int, input().split())

def min2(a, b):
    return a if a > b else b 

def max2(a, b):
    return a if a > b else b 

def mid2(a, b):
    return (a + b) / 2

print(min2(a, b))
print(max2(a, b))
print(f"{mid2(a, b):.2f}")