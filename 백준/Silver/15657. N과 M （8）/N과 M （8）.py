from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
n = list(map(int, input().split()))

ans = []

li = []
def dfs(idx):
    
    if len(li) == M:
        ans.append(sorted(li[:]))
        return
    
    for i in range(idx, N):
        li.append(n[i])
        dfs(i)
        li.pop()

dfs(0)

for i in sorted(ans):
    print(*i)