from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**5)

n = int(input())

tree = dict()

ans = [0] * (n+1)

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    
    if tree.get(parent):
        tree[parent].append(child)
    else:
        tree[parent] = [child]
    
    ans[child] = weight

realAns = float("-inf")
def dfs(root):
    global realAns
    
    for child in tree.get(root):
        if tree.get(child):
            dfs(child)
    
    ans[root] += max(map(lambda x:ans[x], tree.get(root)))
    tmp = sorted(map(lambda x:ans[x], tree[root]))
    tmp = tmp[-1]+tmp[-2] if len(tmp) > 1 else tmp[-1]
    realAns = max(realAns, tmp)

if 1 < n:
    dfs(1)
    print(realAns)
else:
    print(0)