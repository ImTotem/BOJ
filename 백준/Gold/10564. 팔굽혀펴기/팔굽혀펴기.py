import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    dp = [[-1] * 101 for _ in range(n + 1)]
    
    def f(a, b):
        if a == 0: return 0

        if dp[a][b] != -1:
            return dp[a][b]
        dp[a][b] = -INF

        for i in range(m):
            if a - b * s[i] >= 0:
                dp[a][b] = max(dp[a][b], f(a - b * s[i], b + 1) + s[i])
        
        return dp[a][b]
    
    ans = f(n, 1)
    
    return [-1, ans][ans > 0]

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
