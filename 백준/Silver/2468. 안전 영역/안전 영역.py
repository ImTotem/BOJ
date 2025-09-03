import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

def main():
    d = [0, 1, 0, -1, 0]
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    hs = sorted(set(sum(m, [])))
    
    def size():
        cnt = 0
        visited = [[m[y][x] == -1 for x in range(n)] * n for y in range(n)]

        for j in range(n):
            for i in range(n):
                if visited[j][i]: continue
                
                q = deque([(i, j)])
                visited[j][i] = True
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx, ny = x + d[k], y + d[k+1]
                        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((nx, ny))
                
                cnt += 1
        
        return cnt
    
    ans = 1

    for h in hs:
        for y in range(n):
            for x in range(n):
                if m[y][x] == h: m[y][x] = -1

        ans = max(ans, size())
    
    return ans

if __name__ == "__main__":
    print(main())
