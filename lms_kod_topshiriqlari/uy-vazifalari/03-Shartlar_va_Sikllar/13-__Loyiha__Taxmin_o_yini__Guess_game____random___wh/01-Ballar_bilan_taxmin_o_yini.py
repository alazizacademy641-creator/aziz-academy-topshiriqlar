y = int(input())
b = 100
while True:
    t = int(input())
    if t == y:
        print("TOPDINGIZ")
        break
    print("KATTA" if t > y else "KICHIK")
    b = max(0, b - 10)
print(f"Ball: {b}")