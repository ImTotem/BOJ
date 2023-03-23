from sys import stdin
input = stdin.readline

def check(tetromino):
    s = 0
    for y in range(N):
        for x in range(M):
            cur = 0
            for t in tetromino:
                nx, ny = x + t[0], y + t[1]
                if 0 <= nx < M and 0 <= ny < N:
                    cur += paper[ny][nx]
            s = max(s, cur)
    
    return s

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

tetrominos=[
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],
    [(0,0),(1,0),(0,1),(1,1)],
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,1),(1,1),(2,1),(2,0)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(0,1),(1,0),(2,0)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,2),(1,1),(1,2),(1,0)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(1,0),(0,1),(0,2)],
    [(0,0),(1,0),(1,1),(2,1)],
    [(0,1),(1,1),(1,0),(2,0)],
    [(1,0),(1,1),(0,1),(0,2)],
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,1),(1,0),(1,1),(1,2)],
    [(0,0),(0,1),(0,2),(1,1)],
    [(0,0),(1,0),(1,1),(2,0)],
    [(0,1),(1,1),(1,0),(2,1)]
]

ans = 0
for tetromino in tetrominos:
    ans = max(ans, check(tetromino))

print(ans)