import sys
input = lambda:sys.stdin.readline().strip()

DIM = [0, 1, 0, -1, 0]

def main():
    r, c, k = map(int, input().split())
    _map = [list(input()) for _ in range(r)]

    def dfs(x, y):
        if _map[y][x] == k: return x == c-1 and y == 0
        
        cnt = 0
        for i in range(4):
            nx, ny = x + DIM[i], y + DIM[i+1]

            if 0 <= nx < c and 0 <= ny < r and _map[ny][nx] == '.':
                _map[ny][nx] = _map[y][x] + 1
                cnt += dfs(nx, ny)
                _map[ny][nx] = '.'
        
        return cnt
    
    _map[r-1][0] = 1
    print(dfs(0, r-1))

main()