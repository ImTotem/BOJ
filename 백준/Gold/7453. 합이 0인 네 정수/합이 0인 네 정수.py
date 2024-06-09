import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    a, b, c, d = [], [], [], []
    for _ in range(n):
        A, B, C, D = map(int, input().split())
        a.append(A)
        b.append(B)
        c.append(C)
        d.append(D)

    x = dict()

    for i in a:
        for j in b:
            v = i+j
            x[v] = 1 + x[v] if v in x else 1
    
    ans = 0
    for i in c:
        for j in d:
            v = -(i+j)
            if v in x: ans += x[v]
    
    return ans

print(main())