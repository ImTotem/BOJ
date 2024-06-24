import sys
input = lambda:sys.stdin.readline().strip()

from heapq import heappop, heappush

def main():
    n, m = map(int, input().split())

    degree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())

        degree[b] += 1
        heappush(graph[a], b)

    q = []

    for i in range(1, n+1):
        if degree[i] == 0:
            heappush(q, i)
    
    ans = []
    while q:
        cur = heappop(q)
        
        ans.append(cur)

        for g in graph[cur]:
            degree[g] -= 1

            if degree[g] == 0:
                heappush(q, g)

    return ' '.join(map(str, ans))

print(main())