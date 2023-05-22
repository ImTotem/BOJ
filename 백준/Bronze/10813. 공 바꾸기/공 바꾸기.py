import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

ans = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    ans[i], ans[j] = ans[j], ans[i]

print(*ans[1:])