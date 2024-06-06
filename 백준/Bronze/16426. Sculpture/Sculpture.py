import sys
input = lambda:sys.stdin.readline().strip()

D = [0, 1, 0, -1, 0]

def main():
    r, c = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(r)]
    ans = [['0'] * c for _ in range(r)]

    for i in range(1, r-1):
        for j in range(1, c-1):
            a = 1
            for k in range(4):
                a &= grid[i][j] < grid[i+D[k]][j+D[k+1]]
            ans[i][j] = str(a)
    
    return map(lambda x:' '.join(x), ans)

print(*main(), sep="\n")