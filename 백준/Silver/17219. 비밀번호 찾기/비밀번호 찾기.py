from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

in_ = dict()

for _ in range(N):
    a, b = input().split()
    in_[a] = b

for _ in range(M):
    print(in_[input().strip()])