from sys import stdin
input = stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

ans = 0

li = [[1,1], [2, 1]]
def dfs():
    global ans
    
    if li[-1] == [N, N]:
        ans += 1
        return
    
    x1, y1 = li[-2]
    x2, y2 = li[-1]

    nx, ny = x2+1, y2+1
    if nx <= N and ny <= N and house[ny-1][nx-1]+house[ny-2][nx-1]+house[ny-1][nx-2] == 0:
        li.append([nx, ny])
        dfs()
        li.pop()
    
    nx, ny = x2+1, y2
    if nx <= N and ny <= N and x1 + 1 == x2 and house[ny-1][nx-1] == 0:
        li.append([nx, ny])
        dfs()
        li.pop()
    
    nx, ny = x2, y2+1
    if nx <= N and ny <= N and y1+1 == y2 and house[ny-1][nx-1] == 0:
        li.append([nx, ny])
        dfs()
        li.pop()

if house[N-1][N-1] == 1:
    print(0)
else:
    dfs()

    print(ans)