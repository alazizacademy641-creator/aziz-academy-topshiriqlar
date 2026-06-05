login = input()

if login == "admin":
    print("Full access")
elif login == "test":
    print("Guest")
else:
    print("No access")