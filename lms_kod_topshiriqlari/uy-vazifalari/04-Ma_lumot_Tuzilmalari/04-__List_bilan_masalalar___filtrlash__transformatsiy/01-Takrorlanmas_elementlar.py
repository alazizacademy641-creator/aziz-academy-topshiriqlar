elementlar = input().split()

yangi_royxat = []

for x in elementlar:
    if x not in yangi_royxat:
        yangi_royxat.append(x)
        
print(*(yangi_royxat))