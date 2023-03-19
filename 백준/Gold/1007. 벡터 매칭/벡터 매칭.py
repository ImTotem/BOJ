import sys
from itertools import combinations as comb

input = lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    n = int(input())
    pos = [0] * n
    
    xtotal, ytotal = 0, 0

    for i in range(n):
        x, y = map(int, input().split())
        xtotal += x
        ytotal += y
        pos[i] = [x, y]
    
    ans = float("inf")
    c = list(comb(range(n), n//2))
    for i in c[:len(c)//2]:
        xsum, ysum = 0, 0

        for j in i:
            xsum += pos[j][0]
            ysum += pos[j][1]
        
        xsum -= xtotal - xsum
        ysum -= ytotal - ysum

        dis = (xsum**2 + ysum**2) ** 0.5
        ans = min(ans, dis)

    print(ans)