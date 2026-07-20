n = int(input())
positives = [num for _ in range(n) if (num := int(input())) > 0]
print(sum(positives) // len(positives) if positives else 0)
