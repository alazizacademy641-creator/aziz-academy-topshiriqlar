musbat = 0
manfiy = 0
for _ in range(int(input())):
    x = int(input())
    if x > 0:
        musbat += 1
    elif x < 0:
        manfiy += 1
print(musbat, manfiy)