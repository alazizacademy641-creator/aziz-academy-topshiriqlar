n = int(input())
i = 1
count = 0 
stopped = False
while i <= n:
    if i % 2 == 0:
        count += 1
        if count == 3:
            print(i)
            stopped = True
            break
    i += 1
if not stopped:
    print("No")