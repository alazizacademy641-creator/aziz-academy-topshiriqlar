login = input()

parol = input()

check = (len(login) >= 3) and (len(parol) >= 8) and (login != parol)

print(check)