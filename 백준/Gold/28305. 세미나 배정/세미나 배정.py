import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n, t = map(int, input().split())
    a = sorted(map(int, input().split()))

    def flag(k):
        dp = a[:]
        
        for i in range(n):
            dp[i] = max(
                [dp[i-k] + t, 1][i < k],
                1, a[i] - t + 1
            )
            if a[i] < dp[i]: return False
        
        return True
    
    lo, hi = 0, n+1
    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if flag(mid): hi = mid
        else: lo = mid
    
    return hi

print(main())