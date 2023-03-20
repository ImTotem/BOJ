from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
N = list(map(int, input().split()))

cur = sum(N[:k])
ans = cur
for i in range(n-k):
    cur = cur - N[i] + N[i+k]

    if ans < cur:
        ans = cur

print(ans)