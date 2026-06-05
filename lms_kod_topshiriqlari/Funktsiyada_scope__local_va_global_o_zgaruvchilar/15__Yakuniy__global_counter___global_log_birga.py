counter = 0
logs = []

def add(msg):
    global counter, logs
    logs.append(msg)
    counter += 1
    
def stats():
    return f"count={counter}, logs={len(logs)}"

n = int(input())

for _ in range(n):
    msg = input()
    add(msg)
    
print(stats())