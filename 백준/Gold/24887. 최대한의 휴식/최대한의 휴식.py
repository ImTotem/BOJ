import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    w = [0]+list(map(int, input().split()))
    
    if sum(w) < m: return -1
    if m <= max(w): return "Free!"

    ans = 0
    dp = [0] * (n+1)
    lo, hi = 1, n-1

    while (lo <= hi):
        mid = (lo + hi) // 2

        for i in range(1, mid+1): dp[i] = max(dp[i-1], w[i])
        for i in range(mid+1, n+1): dp[i] = max(dp[i-1], w[i]+dp[i-mid])
        
        if m <= dp[n]:
            lo = mid + 1
            ans = max(ans, mid)
        elif dp[n] < m: hi = mid - 1
    
    return ans - 1

print(main())