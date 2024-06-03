import sys
input = lambda:sys.stdin.readline().strip()

D = [0, 1, 0, -1, 0]

def main():
    r, c, n = map(int, input().split())
    cells = [list(input()) for _ in range(r)]

    if n % 2 == 0: return ['O' * c] * r

    b = {(i, j) for i in range(r) for j in range(c) if cells[i][j] == 'O'}
    a = {(i, j) for i in range(r) for j in range(c)}

    for _ in range(1, n, 2):
        tmp = a - b
        for i, j in b:
            for k in range(4):
                tmp -= {(i + D[k], j + D[k+1])}
        
        b = tmp.copy()

    ans = [list("." * c) for _ in range(r)]

    for i, j in b:
        ans[i][j] = 'O'
        
    return map(lambda x:''.join(x), ans)

print(*main(), sep="\n")