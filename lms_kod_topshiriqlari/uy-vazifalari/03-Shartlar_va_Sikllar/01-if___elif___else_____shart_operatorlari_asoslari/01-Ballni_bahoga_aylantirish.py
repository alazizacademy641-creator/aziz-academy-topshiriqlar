ball = int(input())

if ball < 0 or ball > 100:
    print("notogri")
elif 86 <= ball <= 100:
    print(5)
elif 71 <= ball <= 85:
    print(4)
elif 56 <= ball <= 70:
    print(3)
else:
    print(2)