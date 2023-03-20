from sys import stdin
input = stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(s))
else:
    dp = []

    dp.append(s[0])
    dp.append(s[0]+s[1])
    dp.append(max(s[0] + s[2], s[1]+s[2]))

    for i in range(3, n):
        dp.append(max( s[i] + dp[i-2], dp[i-3] + s[i-1] + s[i] ))

    print(dp[-1])