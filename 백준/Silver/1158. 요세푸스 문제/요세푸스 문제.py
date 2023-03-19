from collections import deque
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

seq = deque([n-i for i in range(n)])

ans = []

for _ in range(n):
    seq.rotate(k)
    ans.append(seq.popleft())

print(f"<{str(ans)[1:-1]}>")
