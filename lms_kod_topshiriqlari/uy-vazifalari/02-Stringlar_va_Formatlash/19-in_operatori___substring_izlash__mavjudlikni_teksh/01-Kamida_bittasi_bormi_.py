text = input().strip()
word1 = input().strip()
word2 = input().strip()

result = (word1 in text) or (word2 in text)
print(result)