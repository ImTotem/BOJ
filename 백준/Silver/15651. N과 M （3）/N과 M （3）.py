n, m = list(map(int, input().split()))

s = []

def dfs():
    if len(s) == m:
        print(*s)
    else:
        for i in range(1, n+1):
            s.append(i)
            dfs()
            s.pop()

dfs()