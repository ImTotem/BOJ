import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    r, c, h, w = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(r)]
    mask = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
    acc = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
    
    def ps(m):
        for y in range(r):
            for x in range(c):
                mask[y][x] = (-1, 1)[city[y][x] > m]
                
        for y in range(r):
            for x in range(c):
                acc[y][x] = acc[y-1][x] + acc[y][x-1] - acc[y-1][x-1] + mask[y][x]

        for y in range(h - 1, r):
            for x in range(w - 1, c):
                if acc[y][x] - acc[y-h][x] - acc[y][x-w] + acc[y-h][x-w] <= 0:
                    return True
        return False

    
    lo, hi = 1, r * c
    while lo <= hi:
        mid = (lo + hi) // 2

        if ps(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    
    return lo


if __name__ == "__main__":
    print(main())
