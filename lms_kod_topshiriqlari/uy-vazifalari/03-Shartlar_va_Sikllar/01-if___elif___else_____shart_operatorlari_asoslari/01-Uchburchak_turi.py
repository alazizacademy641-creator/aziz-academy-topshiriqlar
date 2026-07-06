a = int(input())
b = int(input())
c = int(input())
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("teng tomonli")
    elif a == b or a == c or b == c:
        print("teng yonli")
    else:
        print("turli tomonli")
else:
    print("notogri")