import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')
d = [1, 0, -1, 0, 1]

def main():
    n = int(input())
    imgs1 = [input() for _ in range(n)]
    imgs2 = [list(i.replace('R', 'G')) for i in imgs1]
    imgs1 = list(map(list, imgs1))

    def bfs(a, b, graph):
        if graph[b][a] == 0: return 0
        target = graph[b][a]
        q = deque([(a, b)])

        while q:
            x, y = q.popleft()

            graph[y][x] = 0
            
            for i in range(4):
                nx, ny = x + d[i], y + d[i+1]
                
                if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] != 0 and graph[ny][nx] == target:
                    graph[ny][nx] = 0
                    q.append((nx, ny))

        return 1

    normal, color_blind = 0, 0

    for a in range(n):
        for b in range(n):
            normal += bfs(a, b, imgs1)
            color_blind += bfs(a, b, imgs2)

    return f'{normal} {color_blind}'
    
if __name__ == "__main__":
    print(main())
