n = int(input())
max_num = int(input())
for _ in range(n -1):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
print(max_num)