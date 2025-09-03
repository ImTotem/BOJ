import sys
input = lambda: sys.stdin.readline().strip()
from collections import Counter
from math import ceil

INF = float('inf')

def main():
    n = input()
    cnt = Counter(n)
    ans = max(cnt[str(i)] for i in range(10) if i not in {6, 9})
    ans = max(ans, ceil((cnt['6'] + cnt['9']) / 2))

    return ans


if __name__ == "__main__":
    print(main())
