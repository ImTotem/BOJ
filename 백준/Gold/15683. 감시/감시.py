import sys
input = lambda:sys.stdin.readline().strip()

def get_ds(typ):
    a, b, c, d = (0, -1), (1, 0), (0, 1), (-1, 0)
    if typ == 1:
        return [[a], [b], [c], [d]]
    if typ == 2:
        return [[a, c], [b, d]]
    if typ == 3:
        return [[a, b], [b, c], [c, d], [d, a]]
    if typ == 4:
        return [[a, b, d],[a, b, c],[b, c, d],[a, c, d]]
    return [[a, b, c, d]]

def main():
    n, m = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(n)]
    cctvs = [(i, j) for i in range(n) for j in range(m) if 0 < office[i][j] < 6]

    ans = [sum(1 for i in range(n) for j in range(m) if office[i][j] == 0)] * 2

    def rem(idx, d, delt):
        for dr, dc in d:
            r, c = cctvs[idx]
            while 0 <= r < n and 0 <= c < m:
                if office[r][c] == 6: break
                office[r][c] -= delt * (office[r][c] <= 0)
                ans[0] -= delt * (office[r][c] == -(0 < delt))

                r, c = r + dr, c + dc
    
    def dfs(idx):
        if idx == len(cctvs):
            ans[1] = min(ans)
            return
        
        r, c = cctvs[idx]
        for d in get_ds(office[r][c]):
            rem(idx, d, 1)
            dfs(idx+1)
            rem(idx, d, -1)

    dfs(0)

    return ans[1]

print(main())
