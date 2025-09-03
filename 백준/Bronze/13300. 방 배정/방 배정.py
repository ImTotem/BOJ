import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict
from math import ceil

INF = float('inf')

def main():
    n, k = list(map(int, input().split()))
    s = defaultdict(int)

    for _ in range(n):
        s[tuple(map(int, input().split()))] += 1
    
    return sum(ceil(i / k) for i in s.values())

if __name__ == "__main__":
    print(main())
