import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    k, r, n = input().split()
    n = int(n)
    ops = [input() for _ in range(n)]

    a2i = lambda p: '_ABCDEFGH'.index(p[0])
    i2a = lambda p: '_ABCDEFGH'[p[0]]

    D = {
        "R": (1, 0),
        "L": (-1, 0),
        "B": (0, -1),
        "T": (0, 1),
        "RT": (1, 1),
        "LT": (-1, 1),
        "RB": (1, -1),
        "LB": (-1, -1)
    }

    k = (a2i(k), int(k[1]))
    r = (a2i(r), int(r[1]))

    for op in ops:
        dx, dy = D[op]

        nk = (k[0] + dx, k[1] + dy)
        nr = r
        if nk == nr: nr = (r[0] + dx, r[1] + dy)
        if not (1 <= nk[0] <= 8 and 1 <= nk[1] <= 8): continue
        if not (1 <= nr[0] <= 8 and 1 <= nr[1] <= 8): continue

        k, r = nk, nr
    
    return f'{i2a(k)}{k[1]}\n{i2a(r)}{r[1]}'

if __name__ == "__main__":
    print(main())
