from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * M

s = 0
num = 0

for i in range(N):
    s += A[i]
    res = s % M

    if res == 0:
        num += 1

    B[res] += 1

for i in range(M):
    if B:
        num += B[i] * (B[i] - 1) // 2

print(num)