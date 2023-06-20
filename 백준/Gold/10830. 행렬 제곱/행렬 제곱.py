import sys

input = lambda: sys.stdin.readline().strip()

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

def mul(u, v):
    z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += u[row][i] * v[i][col]
            z[row][col] = e % 1000
    
    return z

def square(a, b):
    if b == 1:
        for x in range(n):
            for y in range(n):
                a[x][y] %= 1000
        return a
    
    tmp = square(a, b//2)
    if b % 2:
        return mul(mul(tmp, tmp), a)
    else:
        return mul(tmp, tmp)
    
ans = square(a, b)
for i in ans:
    print(*i)