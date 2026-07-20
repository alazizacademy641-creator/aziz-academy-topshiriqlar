text = input()
spaces_count = 0
for char in text:
    if char == " ":
        spaces_count += 1
words_count = spaces_count + 1
print(words_count)