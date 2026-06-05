a, b, c = map(int, input().split())
if a == b:
    if b == c:
        print("All equal")
    else:
        print("Partially equal")
else:
    if a == c or b == c:
        print("Partially equal")
    else:
        print("Not equal")