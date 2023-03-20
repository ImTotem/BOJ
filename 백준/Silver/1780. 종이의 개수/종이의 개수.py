from sys import stdin
input = stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

result = []

def func(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                func(x, y, n//3)
                func(x, y+n//3, n//3)
                func(x, y+n//3*2 ,n//3)

                func(x+n//3, y, n//3)
                func(x+n//3, y+n//3, n//3)
                func(x+n//3, y+n//3*2, n//3)

                func(x+n//3*2, y, n//3)
                func(x+n//3*2, y+n//3, n//3)
                func(x+n//3*2, y+n//3*2, n//3)
                return

    if color == -1:
        result.append(-1)
    elif color:
        result.append(1)
    else:
        result.append(0)

func(0, 0, n)
for i in (-1, 0, 1):
    print(result.count(i))