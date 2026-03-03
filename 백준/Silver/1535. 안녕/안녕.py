import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    l = list(map(int, input().split()))
    j = list(map(int, input().split()))

    dp = [0] * 100
    
    for i in range(n):
        for k in range(99, l[i] - 1, -1):
            dp[k] = max(dp[k], dp[k - l[i]] + j[i])
    
    return dp[-1]

if __name__ == "__main__":
    print(main())
