import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    r, c, h, w = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(r)]

    maxi = r * c
    mid = (h * w) // 2

    def ps(x, y):
        cs = [0] * (maxi + 1)
        for dy in range(h):
            for dx in range(w):
                cs[city[y + dy][x + dx]] += 1

        cnt = 0
        for i in range(1, maxi + 1):
            cnt += cs[i]
            if cnt > mid:
                return i

    
    return min(ps(x, y) for y in range(r - h + 1) for x in range(c - w + 1))


if __name__ == "__main__":
    print(main())
