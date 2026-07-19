menu = int(input())
n = int(input())

if menu == 1:
    minutes = n // 60
    seconds = n % 60
    print(f"{minutes} minut {seconds} soniya")
elif menu == 2:
          hours = n // 60
          minutes = n % 60
          print(f"{hours} soat {minutes} minut")
else:        
     print("Notogri tanlov")