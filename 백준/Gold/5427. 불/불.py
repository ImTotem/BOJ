import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

def main():
    d = [1, 0, -1, 0, 1]
    w, h = map(int, input().split())
    q = deque()
    fires = deque()
    building = []
    for y in range(h):
        tmp = list(input())
        for x in range(w):
            if tmp[x] == '@':
                q.append((x, y, 0))
                tmp[x] = '.'
            elif tmp[x] == '*':
                fires.append((x, y, 0))
        building.append(tmp)
    
    visited = [[False] * w for _ in range(h)]
    while q:
        x, y, cnt = q.popleft()

        if x in {0, w - 1} or y in {0, h - 1}: return cnt + 1

        while fires and fires[0][2] == cnt:
            fx, fy, fcnt = fires.popleft()

            for i in range(4):
                fnx, fny = fx + d[i], fy + d[i+1]

                if 0 <= fnx < w and 0 <= fny < h and building[fny][fnx] == '.':
                    building[fny][fnx] = '*'
                    fires.append((fnx, fny, fcnt + 1))

        for i in range(4):
            nx, ny = x + d[i], y + d[i+1]
            
            if 0 <= nx < w and 0 <= ny < h and building[ny][nx] == '.' and not visited[ny][nx]:
                q.append((nx, ny, cnt + 1))
                visited[ny][nx] = True

    return "IMPOSSIBLE"
    

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
