n = int(input())
talabalar = []

for _ in range(n):
    ism, ball = input().split()
    ball = int(ball)
    
    talabalar.append((-ball, ism))
    
talabalar.sort()

for ball, ism in talabalar:
    original_ball = -ball
    print(f"{ism} {original_ball}")