list1 = input().split()
list2 = input().split()
set2 = set(list2)
result = []
for x in list1:
    if x in set2 and x not in result:
        result.append(x)
print(*(result))