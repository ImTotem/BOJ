import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

ans = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    ans = ans[:i-1] + ans[i-1:j][::-1] + ans[j:]

print(*ans)