import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

def main():
    MOD = 2147483647
    D = [0, 1, 0, -1, 0]

    n = int(input())
    maze = [list(input()) for _ in range(n)]

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            dp[i][j] += (((0 <= j-1 and dp[i][j-1]) + (0 <= i-1 and dp[i-1][j])) * (maze[i][j] == ".")) % MOD
    
    if dp[-1][-1]: return dp[-1][-1] % MOD

    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        if x == y == n-1: return "THE GAME IS A LIE"

        for i in range(4):
            nx, ny = x + D[i], y + D[i+1]

            if 0 <= nx < n and 0 <= ny < n and maze[ny][nx] == '.':
                q.append((nx, ny))
                maze[ny][nx] = "#"

    return "INCONCEIVABLE"

print(main())