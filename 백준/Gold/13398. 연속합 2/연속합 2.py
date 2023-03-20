from sys import stdin
input = stdin.readline

n = int(input())
b = list(map(int, input().split()))

dp1 = [0]*n
dp1[0] = b[0]

ans = dp1[0]

for i in range(1, n):
    dp1[i] = max(dp1[i-1]+b[i], b[i])

    ans = max(ans, dp1[i])

dp2 = [0]*n
dp2[n-1] = b[n-1]

for i in range(n-2, 0, -1):
    dp2[i] = max(dp2[i+1]+b[i], b[i])

for i in range(1, n-1):
    temp = dp1[i-1] + dp2[i+1]

    ans = max(ans, temp)

print(ans)
