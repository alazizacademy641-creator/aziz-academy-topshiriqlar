email = input()
parol = input()

email_ok = '@' in email and '.' in email and email == email.lower()

parol_ok = 8 <= len(parol) <= 16

print(email_ok and parol_ok)