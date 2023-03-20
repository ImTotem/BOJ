from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
table = [[0]+list(map(int, input().split())) for _ in range(N)]
in_ = [map(int, input().split()) for _ in range(M)]

for i in range(N):
    for j in range(1, N+1):
        table[i][j] += table[i][j-1]

for y1, x1, y2, x2 in in_:
    ans = 0
    for i in range(y1-1, y2):
        ans += table[i][x2] - table[i][x1-1]
    print(ans)