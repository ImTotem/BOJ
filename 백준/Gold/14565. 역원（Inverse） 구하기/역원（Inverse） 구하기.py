import sys

input = lambda: sys.stdin.readline().strip()

n, a = map(int, input().split())

def euclid(x, y):
    if x < y: x, y = y, x
    if y == 0: return x, 1, 0

    g, x1, y1 = euclid(y, x%y)
    return g, y1, x1 - (x // y) * y1

g, x, y = euclid(n, a)
if g != 1:
    print(n-a, -1)
else:
    print(n-a, (y+n)%n)