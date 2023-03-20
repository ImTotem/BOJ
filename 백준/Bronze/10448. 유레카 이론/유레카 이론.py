import sys

input = lambda: sys.stdin.readline().strip()

def solve(n):
    l = int(((8*n+1)**.5+1)//2)
    Tn = list(map(lambda x:x*(x+1)//2, range(1, l+1)))

    for i in range(l):
        for j in range(l):
            for k in range(l):
                if Tn[i] + Tn[j] + Tn[k] == n:
                    return 1
    
    return 0

for _ in range(int(input())):
    k = int(input())

    print(solve(k))