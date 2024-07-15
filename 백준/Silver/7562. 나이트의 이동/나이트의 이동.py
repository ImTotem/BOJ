import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def main():
    l = int(input())

    s = tuple(map(int, input().split()))
    e = tuple(map(int, input().split()))

    q = deque()
    q.append((*s, 0))
    visited = [[False] * l for _ in range(l)]
    visited[s[1]][s[0]] = True
    
    while q:
        x, y, cnt = q.popleft()
        
        if (x, y) == e:
            return cnt
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not visited[ny][nx]:
                q.append((nx, ny, cnt+1))
                visited[ny][nx] = True
    
for _ in range(int(input())):
    print(main())