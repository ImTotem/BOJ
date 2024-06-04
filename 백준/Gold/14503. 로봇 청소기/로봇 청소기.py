import sys
input = lambda:sys.stdin.readline().strip()

D = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

def main():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    
    ans = 0
    
    while True:
        if room[r][c] == 0:
            ans += 1
            room[r][c] = 2
        
        clean = True
        for i in range(4):
            nd = (d + i) % 4
            if room[r + D[nd][1]][c + D[nd][0]] == 0:
                clean = False
                break
        
        if clean:
            nr = r - D[d][1]
            nc = c - D[d][0]
        else:
            d = d-1 + (4 * (d-1 < 0))
            nr = r + D[d][1]
            nc = c + D[d][0]
        
        if 0 <= nr < n and 0 <= nc < m:
            if clean:
                if room[nr][nc] == 1: break
                r, c = nr, nc
            elif room[nr][nc] == 0:
                r, c = nr, nc

    return ans

print(main())
