import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, k = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    items.sort()

    dp = [0] * (k + 1)
    
    for w, v in items:
        for i in range(k, 0, -1):
            if w > i: continue
            dp[i] = max(dp[i], dp[i - w] + v)
    
    return dp[k]


if __name__ == "__main__":
    print(main())
