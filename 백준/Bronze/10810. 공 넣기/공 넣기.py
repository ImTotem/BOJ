import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

ans = [0] * (n+1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for r in range(i, j+1):
        ans[r] = k

print(*ans[1:])