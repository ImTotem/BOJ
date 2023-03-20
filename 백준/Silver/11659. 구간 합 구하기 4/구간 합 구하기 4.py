from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
N = list(map(int, input().split()))

li = [0]

for i in range(n):
    li.append(li[i]+N[i])

for _ in range(m):
    s, e = map(int, input().split())

    print(li[e]-li[s-1])