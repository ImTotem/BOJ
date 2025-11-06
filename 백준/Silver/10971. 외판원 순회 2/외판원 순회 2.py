import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    w = [list(map(int, input().split())) for _ in range(n)]
    
    visited = []
    def dfs(i, cost):
        ans = INF

        if len(visited) + 1 == n:
            if w[i][visited[0]] != 0:
                ans = min(ans, cost + w[i][visited[0]])
            return ans
        
        visited.append(i)

        for j in range(n):
            if j in visited: continue
            if w[i][j] == 0: continue
            ans = min(ans, dfs(j, cost + w[i][j]))
        
        visited.pop()

        return ans
    
    return min(dfs(i, 0) for i in range(n))

if __name__ == "__main__":
    print(main())
