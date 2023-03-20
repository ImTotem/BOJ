from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())

v = sorted([int(input()) for _ in range(n)])
cnts = Counter(v).most_common(2)

print(round(sum(v)/n))
print(v[n//2])

if n > 1:
    if cnts[0][1] == cnts[1][1]:
        print(cnts[1][0])
    else:
        print(cnts[0][0])
else:
    print(cnts[0][0])
print(max(v)-min(v))