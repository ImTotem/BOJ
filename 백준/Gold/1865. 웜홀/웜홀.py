import sys
input = lambda:sys.stdin.readline().strip()

INF = int(1e9)

def bf(n, edges, start):
    dist = [INF] * (n + 1)
    dist[start] = 0

    for i in range(n):
        for cur, nxt, cost in edges:
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if i == n - 1: return "YES"
    
    return "NO"

def main():
    for _ in range(int(input())):
        n, m, w = map(int, input().split())

        edges = []

        for _ in range(m):
            s, e, t = map(int, input().split())
            edges.append((s, e, t))
            edges.append((e, s, t))
        
        for _ in range(w):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t))

        print(bf(n, edges, 1))

main()