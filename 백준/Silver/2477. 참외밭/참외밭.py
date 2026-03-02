import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

INF = float('inf')

def main():
    k = int(input())
    v = []

    for _ in range(6):
        _, b = map(int, input().split())
        v.append(b)
    
    w = max(v)
    a = v.index(w)

    x, y = a - 1, (a + 1) % 6

    mm = v[a] * v[y] - v[a - 2] * v[(y + 2) % 6]

    if v[x] > v[y]:
        mm = v[a] * v[x] - v[(a + 2) % 6] * v[x - 2]

    return mm * k

if __name__ == "__main__":
    print(main())
