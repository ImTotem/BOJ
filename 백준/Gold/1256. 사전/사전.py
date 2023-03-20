import sys

input = lambda: sys.stdin.readline().strip()

N, M, K = map(int, input().split())

dp = [[1] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[N][M] < K:
    print(-1)
else:
    ans = ''
    while True:
        if N == 0 or M == 0:
            ans += 'z'*M + 'a'*N
            break
        
        flag = dp[N-1][M]
        if K <= flag:
            N -= 1
            ans += 'a'
        else:
            K -= flag
            M -= 1
            ans += 'z'
    
    print(ans)