import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n, m = int(input()), int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
    
    start, end = map(int, input().split())

    visited = [[INF, 0] for _ in range(n + 1)]
    visited[start][0] = 0

    pq = [(0, start)]
    while pq:
        cu, u = heappop(pq)

        if cu > visited[u][0]: continue
        
        for cv, v in graph[u]:
            cn = cu + cv
            
            if visited[v][0] > cn:
                visited[v] = [cn, u]
                heappush(pq, (cn, v))
    
    ans = [end]
    while ans[-1] != start:
        ans.append(visited[ans[-1]][1])
        
    print(visited[end][0], len(ans), sep='\n')
    print(*ans[::-1])

if __name__ == "__main__":
    main()
