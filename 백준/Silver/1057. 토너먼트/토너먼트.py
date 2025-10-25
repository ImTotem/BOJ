import sys
input = lambda: sys.stdin.readline().strip()
from math import ceil

INF = float('inf')

def main():
    n, a, b = map(int, input().split())
    a, b = sorted([a, b])
    ans = 1

    while not (a % 2 and a + 1 == b):
        a = ceil(a / 2)
        b = ceil(b / 2)

        ans += 1

    return ans

if __name__ == "__main__":
    print(main())
