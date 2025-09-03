import sys
input = lambda: sys.stdin.readline().strip()
from collections import Counter
from math import ceil

INF = float('inf')

def main():
    n = input().replace('6', '9')
    cnt = Counter(n)
    ans = max(cnt[str(i)] for i in set(range(10))-{9})

    return max(ans, ceil(cnt['9'] / 2))


if __name__ == "__main__":
    print(main())
