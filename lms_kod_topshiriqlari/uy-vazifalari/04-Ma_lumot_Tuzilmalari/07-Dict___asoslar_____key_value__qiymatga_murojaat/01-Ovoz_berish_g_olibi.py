votes = [input() for _ in range(int(input()))]
print(max(dict.fromkeys(votes), key=votes.count))
