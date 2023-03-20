from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
n = deque(list(map(int, input().split())))
idx = deque([i+1 for i in range(N)])

ans = []

for i in range(N):
    rot = [0, 1][n[0] > 0] + -1*(n.popleft())
    ans.append(idx.popleft())

    n.rotate(rot)
    idx.rotate(rot)

print(*ans)