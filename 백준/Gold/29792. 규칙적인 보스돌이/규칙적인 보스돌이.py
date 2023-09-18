from math import ceil

import sys
input = lambda:sys.stdin.readline().strip()

n, m, k = map(int, input().split())
d = [int(input()) for _ in range(n)]
boss = [[0, 0]]+[list(map(int, input().split())) for _ in range(k)]

def knapsack(dmg):
    dp = [0] * (901)

    for i in range(1, k+1):
        t = ceil(boss[i][0] / dmg)
        for j in range(900, 0, -1):
            if t <= j:
                dp[j] = max(dp[j], dp[j - t] + boss[i][1])
    
    return dp[-1]

ans = [knapsack(dmg) for dmg in d]
ans.sort()

print(sum(ans[-m:]))