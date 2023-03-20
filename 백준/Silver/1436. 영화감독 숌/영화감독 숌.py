from sys import stdin
input = stdin.readline

n = int(input())

cnt = 1
ans = 666
while cnt < n:
    ans += 1
    if "666" in str(ans):
        cnt+=1

print(ans)
