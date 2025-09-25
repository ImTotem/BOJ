import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0

    visited = [0] * 100_001
    l = 0
    for r in range(n):
        while visited[a[r]] >= k:
            visited[a[l]] -= 1
            l += 1
        ans = max(ans, r - l + 1)
        visited[a[r]] += 1

    return ans

if __name__ == "__main__":
    print(main())
