import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    cells = [list(map(int, list(input()))) for _ in range(n)]

    ans = 0

    for d in range(min(n, m)):
        for y in range(n-d):
            for x in range(m-d):
                if len({cells[y][x], cells[y+d][x], cells[y][x+d], cells[y+d][x+d]}) == 1:
                    ans = max(ans, (d+1)**2)

    return ans

if __name__ == "__main__":
    print(main())
