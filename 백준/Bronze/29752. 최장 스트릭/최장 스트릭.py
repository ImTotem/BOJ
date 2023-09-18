import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
s = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(n):
    if s[i] == 0:
        ans = max(ans, cnt)
        cnt = 0
    else:
        cnt += 1

print(max(ans, cnt))
