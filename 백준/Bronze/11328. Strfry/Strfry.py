import sys
input = lambda: sys.stdin.readline().strip()
from collections import Counter

INF = float('inf')

def main():
    a, b = map(Counter, input().split())
    return ('Impossible', 'Possible')[a == b]

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
