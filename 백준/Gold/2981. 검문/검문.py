import math, re
from sys import stdin
input = stdin.readline

n = int(input())
ns = list(int(input()) for _ in range(n))

ns.sort()

ans = []

t = [ns[i] - ns[i-1] for i in range(1, n)]
g = t[0]

for i in range(1, n-1):
    g = math.gcd(g, t[i])

for i in range(1, int(math.sqrt(g))+1):
    if g % i == 0:
        if i ** 2 == g:
            ans.append(i)
        else:
            ans += [i, g // i]

ans.remove(1)
ans.sort()

print(*ans)