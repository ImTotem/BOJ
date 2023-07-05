import sys
input = lambda:sys.stdin.readline().strip()

INF = float('inf')
x1, y1, x2, y2 = INF, INF, -INF, -INF

for _ in range(int(input())):
    x, y = map(int, input().split())
    
    x1, y1, x2, y2 = min(x1, x), min(y1, y), max(x2, x), max(y2, y)

print((x2-x1)*(y2-y1))