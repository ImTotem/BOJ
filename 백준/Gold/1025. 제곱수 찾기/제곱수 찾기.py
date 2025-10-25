import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]

    def func(x):
        if int(x ** .5) ** 2 == x:
            return x

        return -1

    def cand(x, y, dx, dy):
        ans = -1
        if dx == 0 and dy == 0: return func(int(table[y][x]))
        ret = ''
        while 0 <= x < m and 0 <= y < n:
            ret += table[y][x]
            x += dx
            y += dy

            ans = max(ans, func(int(ret)), func(int(ret[::-1])))
        
        return ans

    ans = -1

    for dy in range(-n - 1, n + 1):
        for dx in range(-m - 1, m + 1):
            for y in range(n):
                for x in range(m):
                    ans = max(ans, cand(x, y, dx, dy))

    return ans
    
if __name__ == "__main__":
    print(main())
