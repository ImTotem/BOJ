from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
ra = sorted(list(map(int, input().split())))

data = { i:ra.count(i) for i in set(ra) }

a = deque([ra[0]])
data[a[-1]]-=1
while ra:
    last = a[-1]
    if data.get(last+1):
        a.append(last+1)
        data[last+1]-=1
    elif data.get(last-1):
        a.append(last-1)
        data[last-1]-=1
    else:
        break

if len(a) == n:
    if abs(a[0] - a[-1]) == 1:
        print(1)
    else:
        print(-1)
else:
    print(-1)