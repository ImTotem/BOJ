import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

def main():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        return None
    
    building = [[] for _ in range(l)]

    q = deque()

    for z in range(l):
        for y in range(r):
            tmp = list(input())
            if 'S' in tmp:
                q.append((tmp.index('S'), y, z, 0))
                tmp[q[0][0]] = '#'
            building[z].append(tmp)
        input()

    while q:
        x, y, z, cnt = q.popleft()

        if building[z][y][x] == 'E':
            return f'Escaped in {cnt} minute(s).'

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l and building[nz][ny][nx] != '#':
                q.append((nx, ny, nz, cnt + 1))
                if building[nz][ny][nx] != 'E': building[nz][ny][nx] = '#'

    return 'Trapped!'
    
if __name__ == "__main__":
    while (out := main()) != None:
        print(out)
