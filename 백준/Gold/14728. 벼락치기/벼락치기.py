import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, t = map(int, input().split())
    
    dp = [0] * (t + 1)
    for i in range(n):
        k, s = map(int, input().split())
        
        for j in range(t, k - 1, -1):
            dp[j] = max(dp[j], dp[j - k] + s)
        
    return dp[-1]

if __name__ == "__main__":
    print(main())
