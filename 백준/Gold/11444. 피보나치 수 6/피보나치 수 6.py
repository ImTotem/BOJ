import sys
input = lambda:sys.stdin.readline().strip()

MOD = 1000000007

def p(a, b):
    c = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= MOD
    return c

def main():
    n = int(input())

    ans = [[1, 0], [0, 1]]
    a = [[1, 1], [1, 0]]

    while 0 < n:
        if n % 2 == 1: ans = p(ans, a)
        a = p(a, a)
        n //= 2
    
    print(ans[0][1])

main()