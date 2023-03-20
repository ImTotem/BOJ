from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = {input()[:-1]:1 for _ in range(n)}

ans = []
for i in range(m):
    b = input()[:-1]

    if a.get(b):
        ans.append(b)

print(len(ans))
for i in sorted(ans):
    print(i)