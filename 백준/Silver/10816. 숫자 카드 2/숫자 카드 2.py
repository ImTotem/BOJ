from sys import stdin
input = stdin.readline

n = int(input())

d = dict()
for i in map(int, input().split()):
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] += 1

m = int(input())
print(*[d.get(i) if d.get(i) != None else 0 for i in map(int, input().split())])