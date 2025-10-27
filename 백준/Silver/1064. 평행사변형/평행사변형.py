import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    ax, ay, bx, by, cx, cy = map(int, input().split())
    a, b, c = (ax, ay), (bx, by), (cx, cy)
    
    if (by - ay) * (cx - bx) == (cy - by) * (bx - ax) : return -1

    ss = lambda p, q: (p - q) ** 2
    dist = lambda p, q: (ss(p[0], q[0]) + ss(p[1], q[1])) ** .5
    f = lambda p, q, r: 2 * (dist(p, q) + dist(q, r))
    
    li = [f(a, b, c), f(b, c, a), f(c, a, b)]

    return max(li) - min(li)


if __name__ == "__main__":
    print(main())
