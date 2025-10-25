import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    ps = [tuple(map(int, input().split())) for _ in range(m)]
    
    minp = min(min(p, 6 * s) for p, s in ps)
    mins = min(i[1] for i in ps)
    
    return minp * (n // 6) + min((n % 6) * mins, minp)


if __name__ == "__main__":
    print(main())
