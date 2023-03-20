from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
s = set(input()[:-1] for _ in range(n))
c = list(input()[:-1] for _ in range(m))

cnt = 0
for i in c:
    if i in s:
        cnt+=1
print(cnt)