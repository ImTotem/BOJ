import sys
input = lambda:sys.stdin.readline().strip()

from collections import defaultdict

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    a, b, c, d = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
    ab = ccw(*a, *b, *c) * ccw(*a, *b, *d)
    cd = ccw(*c, *d, *a) * ccw(*c, *d, *b)
    
    if ab == 0 and cd == 0:
        if a > b: a, b = b, a
        if c > d: c, d = d, c
        return c <= b and a <= d

    return ab <= 0 and cd <= 0

def main():
    n = int(input())
    root = list(range(n))

    lines = [tuple(map(int, input().split())) for _ in range(n)]

    def find(x):
        if root[x] == x: return x

        root[x] = find(root[x])
        return root[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        
        if x < y: root[y] = x
        else: root[x] = y
    
    for i in range(n):
        for j in range(i):
            if is_cross(*lines[i], *lines[j]):
                union(i, j)

    ans = defaultdict(int)
    for i in root:
        ans[find(i)] += 1
    
    return f"{len(ans)}\n{max(ans.values())}"

if __name__ == "__main__": 
    print(main())
