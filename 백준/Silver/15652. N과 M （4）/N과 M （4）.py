from sys import stdin
input = stdin.readline

n, m = list(map(int, input().split()))

s = []

def dfs():
    if len(s) == m:
        print(*s)
    else:
        for i in range(1, n+1):
            if (not len(s)) or s[-1] <= i:
                s.append(i)
                dfs()
                s.pop()

dfs()