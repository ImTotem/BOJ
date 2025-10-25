import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    ans = 0
    n = int(input())
    graph = [input() for _ in range(n)]
    
    for i in range(n):
        friends = set()
        for j in range(n):
            if graph[i][j] == 'N': continue

            friends.add(j)
            friends |= {k for k in range(n) if graph[j][k] == 'Y'}

        ans = max(ans, len(friends) - 1)

    return ans

if __name__ == "__main__":
    print(main())
