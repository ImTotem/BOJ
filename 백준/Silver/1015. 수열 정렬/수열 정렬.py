import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())
A = list(map(int, input().split()))

sA = sorted(A)

P = []
for i in A:
    idx = sA.index(i)
    P.append(idx)
    sA[idx] = -1

print(*P)