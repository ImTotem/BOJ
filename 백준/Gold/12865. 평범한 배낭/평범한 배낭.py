from sys import stdin
input = stdin.readline

N, K = map(int, input().split()) # N: 물품의 수, K: 무게
obj = [[0, 0]]+[list(map(int, input().split())) for _ in range(N)]
# obj = [ [무게, 가치], ... ]

dp = [0] * (K+1)

for i in range(1, N+1):
    for j in range(K, 0, -1):
        if obj[i][0] <= j:
            dp[j] = max(dp[j], dp[j - obj[i][0]] + obj[i][1])

print(dp[K])