price = float(input())
if price >= 200:
    if price >= 500:
        price = price * 0.8
    else:
        price = price * 0.9
print(price)