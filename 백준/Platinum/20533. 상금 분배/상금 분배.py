import sys
input = lambda:sys.stdin.readline().strip()

from bisect import bisect_left

def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    
    dp, idx = [0] * n, [0] * n
    dp[3] = float('-inf')
    for i in range(4, n-2):
        dp[i] = -a[i] + a[i-1] + a[i-2] + a[i-3] + a[i-4]
        idx[i] = i
        if dp[i-1] > dp[i]:
            dp[i] = dp[i-1]
            idx[i] = idx[i-1]

    ans = -1
    for i in range(5, n - 1): # p2 인덱스
        for j in range(idx[i-1], i): # p3 인덱스
            left = a[j-1] + a[j-2] + a[j-3] + a[j-4]
            mid = a[j] + a[i]
            
            if left <= mid: continue

            r = bisect_left(a, mid, lo=i+1)
            
            if r != i+1:
                right = a[r-1]
                ans = max(ans, left + mid + right)

    return ans

print(main())