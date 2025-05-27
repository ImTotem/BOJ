import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    first = [tuple(map(int, input().split())) for _ in range(n)]
    second = [tuple(map(int, input().split())) for _ in range(n)]
    x1, y1 = INF, INF
    for x, y in first:
        x1, y1 = min(x1, x), min(y1, y)
    
    x2, y2 = INF, INF
    for x, y in second:
        x2, y2 = min(x2, x), min(y2, y)

    return f'{x2-x1} {y2-y1}'

if __name__ == "__main__":
    print(main())
