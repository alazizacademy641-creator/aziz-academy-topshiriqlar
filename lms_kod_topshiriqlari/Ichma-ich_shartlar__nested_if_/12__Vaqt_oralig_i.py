hour = int(input())
if hour >= 0:
    if hour <= 5:
        print("Night")
    else:
        if hour <= 11:
            print("Day")
        else:
            if hour <= 17:
                print("Afternoon")
            else:
                print("Evening")