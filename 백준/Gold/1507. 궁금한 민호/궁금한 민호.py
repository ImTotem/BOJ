import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    exist = [[1] * n for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or k == j: continue
                
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    return -1

                if graph[i][j] == graph[i][k] + graph[k][j]:
                    exist[i][j] = 0
    
    return sum(graph[i][j] for i in range(n) for j in range(i + 1, n) if exist[i][j])


if __name__ == "__main__":
    print(main())
