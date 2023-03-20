from sys import stdin
input = stdin.readline

n, m = list(map(int, input().split()))

s = []

def dfs():
    if len(s) == m:
        print(*s)

    for i in range(1, n+1):
        if i not in s:
            if (not len(s)) or max(s) < i:
                s.append(i)
                dfs()
                s.pop()

dfs()