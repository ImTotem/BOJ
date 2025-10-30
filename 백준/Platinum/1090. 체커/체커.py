import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    ps, xs, ys = [], [], []

    for _ in range(n):
        x, y = tuple(map(int, input().split()))
        ps.append((x, y))
        xs.append(x)
        ys.append(y)
    
    ans = [INF] * n

    for mx in xs:
        for my in ys:
            dist = [abs(mx - x) + abs(my - y) for x, y in ps]
            dist.sort()

            d = 0
            for i in range(n):
                d += dist[i]
                ans[i] = min(d, ans[i])

    return ' '.join(map(str, ans))

if __name__ == "__main__":
    print(main())
