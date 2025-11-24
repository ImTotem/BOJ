import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

INF = float('inf')

def main():
    n = int(input())
    chess = [list(map(int, input().split())) for _ in range(n)]

    l = 2*n-1
    ans = 0

    lst = [[] for _ in range(l)]
    visited = [0] * l

    for i in range(n):
        for j in range(n):
            if chess[i][j]:
                lst[i+j].append((i, j))
    
    def dfs(k, cnt):
        nonlocal ans

        if k >= l:
            ans = max(ans, cnt)
            return
        
        for i, j in lst[k]:
            if visited[i-j] == 0:
                visited[i-j] = 1
                dfs(k+2, cnt+1)
                visited[i-j] = 0
        
        dfs(k+2, cnt)
    
    dfs(0, 0)
    t = ans
    ans = 0
    dfs(1, 0)

    return t + ans
    

if __name__ == "__main__":
    print(main())
