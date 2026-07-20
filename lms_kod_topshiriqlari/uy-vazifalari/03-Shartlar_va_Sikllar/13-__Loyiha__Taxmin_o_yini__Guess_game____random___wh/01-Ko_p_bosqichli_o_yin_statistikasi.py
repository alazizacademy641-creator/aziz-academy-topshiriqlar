natija = []
for i in range(1, int(input()) + 1):
    yashirin, u = int(input()), 1
    while int(input()) != yashirin: u += 1
    print(f"Round {i}: {u} urinish")
    natija.append(u)
print(f"Jami: {sum(natija)}\nEng yaxshi: {min(natija)}")