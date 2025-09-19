import sys
input = lambda: sys.stdin.readline().strip()
from bisect import bisect_left

INF = float('inf')

def main():
    n = int(input())
    sqn = n*n
    values = sum([list(map(int, input().split())) for _ in range(n)], [])
    keys = sorted(range(sqn), key=lambda x:values[x])
    
    D = (1, -1, n, -n)

    dp = [1] * sqn
    for k in keys:
        x, y = k // n, k % n
        for d in D:
            nk = k + d
            nx, ny = nk // n, nk % n
            if 0 <= nk < sqn and abs(x - nx) + abs(y - ny) == 1 and values[k] < values[nk]:
                dp[nk] = max(dp[nk], dp[k] + 1)

    return max(dp)

if __name__ == "__main__":
    print(main())
