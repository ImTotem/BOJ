import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    ans = [['-'] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for _ in range(m):
        i, j, cost = map(int, input().split())
        graph[i-1][j-1] = cost
        graph[j-1][i-1] = cost
        ans[i-1][j-1] = str(j)
        ans[j-1][i-1] = str(i)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    ans[i][j] = ans[i][k]

    return '\n'.join(' '.join(i) for i in ans)

if __name__ == "__main__":
    print(main())
