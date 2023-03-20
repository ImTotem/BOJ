from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
n = list(map(int, input().split()))

ans = []

li = []
def dfs():
    
    if len(li) == M:
        ans.append(li[:])
    
    for i in n:
        if i not in li:
            li.append(i)
            dfs()
            li.pop()

dfs()

for i in sorted(ans):
    print(*i)