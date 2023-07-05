import sys
input = lambda:sys.stdin.readline().strip()

a, b, c, d, e, f = map(int, input().split())

def ans():
    for y in range(-999, 1000):
        for x in range(-999, 1000):
            if a*x+b*y == c and d*x+e*y == f:
                print(x, y)
                return

ans()