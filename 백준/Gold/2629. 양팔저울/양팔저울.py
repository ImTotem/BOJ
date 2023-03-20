import sys

input = lambda: sys.stdin.readline().strip()

weight = int(input())
w = list(map(int, input().split()))
ball = int(input())
b = list(map(int, input().split()))

dp = [[False] * (15001) for _ in range(weight + 1)]

res = set()

def dfs(now, l, r):
    
    new = abs(l - r)

    if new not in res:
        res.add(new)
    
    if now == weight:
        return 0

    if not dp[now][new]:
        dfs(now+1, l + w[now], r)
        dfs(now+1, l, r + w[now])
        dfs(now+1, l, r)
        dp[now][new] = True

dfs(0, 0, 0)

print(' '.join(['N','Y'][i in res] for i in b))