kiritilgan_matn = input().split()

sonlar_tup = tuple(int(x) for x in kiritilgan_matn)

yigindi = 0
for son in sonlar_tup:
    yigindi += son
    
print(yigindi)