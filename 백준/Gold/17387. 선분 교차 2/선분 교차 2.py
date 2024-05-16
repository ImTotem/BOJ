import sys
input = lambda:sys.stdin.readline().strip()

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    ccw = lambda x1, y1, x2, y2, x3, y3: (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

    a, b = sorted([(x1, y1), (x2, y2)])
    c, d = sorted([(x3, y3), (x4, y4)])

    if (ccw(*a, *b, *c) * ccw(*a, *b, *d) <= 0\
    and ccw(*c, *d, *a) * ccw(*c, *d, *b) <= 0)\
    and (a <= d and b >= c):
        return 1

    return 0

print(main())