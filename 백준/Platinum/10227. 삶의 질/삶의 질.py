import sys
input = lambda: sys.stdin.readline().strip()
from collections import Counter

INF = float('inf')

def main():
    r, c, h, w = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(r)]

    mid = h * w // 2
    
    def ps(x, y):
        seg = [city[y + dy][x + dx] for dy in range(h) for dx in range(w)]
        seg.sort()
        return seg[mid]
    
    return min(ps(x, y) for y in range(r - h + 1) for x in range(c - w + 1))


if __name__ == "__main__":
    print(main())
