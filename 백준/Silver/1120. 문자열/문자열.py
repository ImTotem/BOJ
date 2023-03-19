import sys

input = lambda: sys.stdin.readline().strip()

a, b = input().split()
la, lb = len(a), len(b)

ans = lb
for start in range(lb - la+1):
    d = 0
    for i in range(la):
        if a[i] != b[start+i]:
            d += 1
    
    if d < ans: ans = d

print(ans)