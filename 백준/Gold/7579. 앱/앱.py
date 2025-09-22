import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    am = list(map(int, input().split()))
    ac = list(map(int, input().split()))
    c = sum(ac)

    ans = c
    dp = [0] * (c + 1)
    for i in range(n):
        for j in range(c, -1, -1):
            if ac[i] > j: continue
            dp[j] = max(dp[j], dp[j - ac[i]] + am[i])
            if dp[j] >= m: ans = min(ans, j)
    
    return ans

if __name__ == "__main__":
    print(main())
