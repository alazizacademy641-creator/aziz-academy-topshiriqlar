text = input()
words = text.replace(',', ' ').split()
print(' '.join(words))
print(len(words))
