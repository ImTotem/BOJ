import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
s = list(map(int, input().split()))

cur = 0
ans = float("-inf")

for i in s:
    cur = max(cur + i, i)
    ans = max(ans, cur)

print(ans)