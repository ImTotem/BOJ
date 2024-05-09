import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    am = list(map(int, input().split()))
    ac = list(map(int, input().split()))
    w = sum(ac) + 1

    dp0, dp1 = [0] * w, [0] * w
    ans = w

    for i in range(n):
        dp0 = dp1[:]
        for j in range(ac[i], w):
            dp1[j] = max(am[i] + dp0[j-ac[i]], dp1[j])
            if m <= dp1[j]: ans = min(ans, j)
    
    return ans

print(main())