import sys
input = lambda: sys.stdin.readline().strip()
from bisect import bisect_left

INF = float('inf')

def main():
    n, m = map(int, input().split())
    am = list(map(int, input().split()))
    ac = list(map(int, input().split()))
    c = sum(ac)

    dp = [0] * (c + 1)
    for i in range(n):
        for j in range(c, -1, -1):
            if ac[i] > j: continue
            dp[j] = max(dp[j], dp[j - ac[i]] + am[i])
    
    return min(c, bisect_left(dp, m))

if __name__ == "__main__":
    print(main())
