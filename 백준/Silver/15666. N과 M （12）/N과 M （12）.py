N, M = map(int, input().split())
n = list(sorted(set(map(int, input().split()))))
N = len(n)

ans = []

li = []
def dfs(idx):
    if len(li) == M:
        ans.append(li[:])
    else:
        for i in range(idx, N):
            li.append(n[i])
            dfs(i)
            li.pop()

dfs(0)

for i in ans:
    print(*i)