from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
loc = deque(list(map(int, input().split())))

d = deque(list(range(1, n+1)))

cnt = 0
while loc:
    if d[0] == loc[0]:
        d.popleft()
        loc.popleft()
        n-=1
    else:
        s = d.index(loc[0])
        _min = min(n-s, s)
        cnt+=_min
        d.rotate(-1*_min if s == _min else _min)
print(cnt)