menu = int(input())
ball = int(input())
if menu == 1:
    if ball >= 90:
        print("A")
    elif ball >= 80:
        print("B")
    elif ball >= 70:
        print("C")
    elif ball >= 60:
        print("D")
    else:
        print("F")
elif menu == 2:
    if ball >= 60:
        print("O'tdi")
    else:
        print("Yiqildi")
else:
    print("Notogri tanlov")