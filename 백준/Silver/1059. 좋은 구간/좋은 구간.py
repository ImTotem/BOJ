import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    l = map(int, input().split())
    s = set(map(int, input().split()))
    n = int(input())

    ans = 0

    for a in range(1, 1000):
        for b in range(a + 1, 1001):
            if n < a or b < n: continue
            if s & set(range(a, b + 1)): continue

            ans += 1

    return ans

if __name__ == "__main__":
    print(main())
