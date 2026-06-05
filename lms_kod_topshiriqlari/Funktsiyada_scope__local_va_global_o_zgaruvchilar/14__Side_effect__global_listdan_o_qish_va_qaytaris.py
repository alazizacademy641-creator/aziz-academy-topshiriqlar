nums = []

def push(x):
    nums.append(x)
    
def last():
    if len(nums) == 0:
        print("NONE")
    else:
        print(nums[-1])
        
q = int(input())
        
for _ in range(q):
    cmd = input().split()
    
    if cmd[0] == "push":
        push(int(cmd[1]))
    else:
        last()