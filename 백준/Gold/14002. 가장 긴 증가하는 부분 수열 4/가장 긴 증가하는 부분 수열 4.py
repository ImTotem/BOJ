from bisect import bisect_left as search
import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
a = list(map(int, input().split()))

dp, idx, ans = [], [], []

for i in a:
    cur = search(dp, i)
    if len(dp) <= cur:
        dp.append(i)
    else:
        dp[cur] = i
    idx.append(cur)

m = max(idx)
for i in range(len(idx)-1, -1, -1):
    if idx[i] == m:
        ans.append(a[i])
        m-=1

print(len(ans))
print(*ans[::-1])
