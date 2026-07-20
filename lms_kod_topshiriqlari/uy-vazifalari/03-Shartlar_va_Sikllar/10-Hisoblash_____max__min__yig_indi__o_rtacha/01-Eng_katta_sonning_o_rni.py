n = int(input())
numbers = [int(input()) for _ in range(n)]
print(numbers.index(max(numbers)) + 1)