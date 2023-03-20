from sys import stdin
input = stdin.readline

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt+=1
    ans.append(str(cnt))

print( ' '.join(i for i in ans ) )