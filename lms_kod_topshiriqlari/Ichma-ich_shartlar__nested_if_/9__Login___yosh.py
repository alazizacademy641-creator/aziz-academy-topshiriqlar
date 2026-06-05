login, age = input().split()
age = int(age)
if login == "admin":
    if age >= 18:
        print("Full access")
    else:
        print("Limit access")
else:
    print("No access")