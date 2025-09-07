import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque
from itertools import combinations as comb

INF = float('inf')
d = [1, 0, -1, 0, 1]

def main():
    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]
    not_wall_cnt = 0
    two = []
    for i in range(n):
        for j in range(n):
            not_wall_cnt += lab[i][j] != 1
            if lab[i][j] == 2:
                two.append((j, i, 0))

    def bfs(starts):
        time = 0
        cnt = m

        visited = [[False] * n for _ in range(n)]
        for x, y, _ in starts:
            visited[y][x] = True

        q = deque(starts)
        while q:
            x, y, t = q.popleft()
            
            for i in range(4):
                nx, ny = x + d[i], y + d[i+1]

                if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and lab[ny][nx] != 1:
                    q.append((nx, ny, t + 1))
                    visited[ny][nx] = True
                    cnt += 1
                    time = max(time, t + 1)
        
        return time, not (not_wall_cnt - cnt)
    
    ans = INF
    for starts in comb(two, m):
        t, res = bfs(starts)
        if res: ans = min(ans, t)

    return ans if ans != INF else -1
    
if __name__ == "__main__":
    print(main())
