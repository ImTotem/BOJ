import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    cnt = 1
    ans = []
    while (n := int(input())) != 0:
        graph = [list(map(int, input().split())) for _ in range(n)]
        
        pq = [(graph[0][0], 0, 0)] # cost, x, y
        visited = [[INF] * n for _ in range(n)]
        visited[0][0] = graph[0][0]

        while pq:
            c, x, y = heappop(pq)
            
            if c > visited[y][x]: continue

            for i in range(4):
                nx, ny = x + D[i], y + D[i + 1]

                if not (0 <= nx < n and 0 <= ny < n): continue
                
                nc = c + graph[ny][nx]
                if visited[ny][nx] > nc:
                    heappush(pq, (nc, nx, ny))
                    visited[ny][nx] = nc
        
        ans.append(f'Problem {cnt}: {visited[-1][-1]}')
        cnt += 1

    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
