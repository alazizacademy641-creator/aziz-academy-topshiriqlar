elements = input().split()
p = int(input())
x = input()
elements.insert(p, x)

print(*elements)