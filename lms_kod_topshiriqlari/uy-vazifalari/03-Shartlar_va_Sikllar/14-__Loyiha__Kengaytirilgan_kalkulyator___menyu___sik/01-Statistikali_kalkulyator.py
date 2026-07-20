import sys
d = list(map(int, sys.stdin.read().split()))
i = c = s = 0
while i < len(d) and d[i] != 0:
    op, a, b = d[i], d[i+1], d[i+2]
    i += 3
    r = (a+b if op==1 else a-b if op==2 else a*b if op==3 else a//b if op==4 and b else None)
    if r is not None:
        print(r); c += 1; s += r 
print(f"Amallar: {c}\nNatijalar yig'indisi: {s}")