import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    rot_info = [tuple(map(int, input().split())) for _ in range(k)]

    def rotate(mat, r, c, s):
        r, c = r-1, c-1
        for d in range(1, s+1):
            v1, v2, v3, v4 = mat[r-d][c-d], mat[r-d][c+d], mat[r+d][c+d], mat[r+d][c-d]

            for i in range(2*d-1):
                mat[r-d+i][c-d] = mat[r-d+i+1][c-d]
                mat[r+d][c-d+i] = mat[r+d][c-d+i+1]
                mat[r+d-i][c+d] = mat[r+d-i-1][c+d]
                mat[r-d][c+d-i] = mat[r-d][c+d-i-1]

            mat[r-d][c-d+1] = v1
            mat[r-d+1][c+d] = v2
            mat[r+d][c+d-1] = v3
            mat[r+d-1][c-d] = v4
        
        return mat
    
    ans = float('inf')

    used = set()
    def dfs(mat):
        nonlocal ans
        if len(used) == k:
            ans = min(ans, min(map(sum, mat)))
            return

        for i in range(k):
            if i not in used:
                used.add(i)
                dfs(rotate([j[::] for j in mat], *rot_info[i]))
                used.discard(i)

    dfs([i[::] for i in a])

    print(ans)

main()