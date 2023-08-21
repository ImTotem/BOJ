import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())

d = dict()
for _ in range(n):
    w = input()
    if m <= len(w):
        d[w] = d[w] + 1 if w in d else 1

print(*sorted(d.keys(),key=lambda x:(-d[x],-len(x),x)),sep="\n")