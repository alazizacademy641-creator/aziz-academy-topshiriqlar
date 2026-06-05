# Bankomatdan pul yechish
# Kurs: IT Dasturlash
# Mavzu: for sikli va range()
# Ball: 100
# Aziz Academy — AI Topshiriq

bankomat_pul = int(input())
n = int(input())

for i in range(1, n + 1):
    summa = int(input())
    
    if bankomat_pul >= summa:
        bankomat_pul -= summa
        print(f"Mijoz {i}: {summa} so'm yechildi. Qoldi: {bankomat_pul} so'm")