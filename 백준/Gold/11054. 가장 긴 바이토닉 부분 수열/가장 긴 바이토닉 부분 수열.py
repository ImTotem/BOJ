from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

lis = [0] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and lis[i] < lis[j]:
            lis[i] = lis[j]
    lis[i] += 1

lis2 = [0] * N

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j] and lis2[i] < lis2[j]:
            lis2[i] = lis2[j]
    lis2[i] += 1

ans = [lis[i] + lis2[i] - 1 for i in range(N)]
print(max(ans))