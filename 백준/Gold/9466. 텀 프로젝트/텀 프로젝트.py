import sys
input = lambda:sys.stdin.readline().strip()
sys.setrecursionlimit(10**8)

def main():
    n = int(input())
    stu = [0] + list(map(int, input().split()))
    
    res = []
    visited = [True] + [False] * n

    def dfs(cur):
        visited[cur] = True
        cycle.append(cur)
        nxt = stu[cur]

        if visited[nxt]:
            if nxt in cycle: res.extend(cycle[cycle.index(nxt):])
        else:
            dfs(nxt)

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(res))

for _ in range(int(input())):
    main()