from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    print(*map(lambda x:sum(x), zip(A[i], list(map(int, input().split())))))