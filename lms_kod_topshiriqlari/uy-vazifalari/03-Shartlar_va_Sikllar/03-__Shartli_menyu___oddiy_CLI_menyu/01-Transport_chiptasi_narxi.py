transport = int(input())
toifa = int(input())

narxlar = {1: 1700, 2: 1700, 3: 4000}

if transport not in narxlar:
    print("Notogri transport")
elif toifa not in [1, 2, 3]:
    print("Notogri toifa")
else:
    baza = narxlar[transport]
    if toifa == 1:
        print(baza)
    elif toifa == 2:
        print(baza // 2)
    elif toifa == 3:
        print(0)