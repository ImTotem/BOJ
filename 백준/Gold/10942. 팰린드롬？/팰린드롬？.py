import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    N = list(map(int, input().split()))

    dp = [[int(i==j) for j in range(n)] for i in range(n)]
    
    for i in range(n-1):
        if N[i] == N[i+1]: dp[i][i+1] = 1
    
    for r in range(2, n):
        for s in range(n-r):
            if N[s] == N[e:=s+r] and dp[s+1][e-1]: dp[s][e] = 1

    for _ in range(int(input())):
        s, e = map(int, input().split())
        print(dp[s-1][e-1])

main()