import sys
input = lambda:sys.stdin.readline().strip()
sys.setrecursionlimit(10**8)

D = [0, 1, 0, -1, 0]

m, n = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

def main(x, y):

    if x+1 == n and y+1 == m: return 1

    if dp[y][x] != -1: return dp[y][x]
    
    ans = 0
    for i in range(4):
        nx, ny = x+D[i], y + D[i+1]
        
        if 0 <= nx < n and 0 <= ny < m and MAP[ny][nx] < MAP[y][x]:
            ans += main(nx, ny)
    dp[y][x] = ans
    return ans

print(main(0, 0))