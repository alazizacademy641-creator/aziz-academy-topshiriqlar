temperatura = int(input())
if temperatura > 30:
    print("Hot")
elif temperatura >= 15 and temperatura <= 30:
    print("Normal")
else:
    print("Cold")