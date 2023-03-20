from sys import stdin
input = stdin.readline

n = int(input())

x = list(map(int, input().split()))
xp = sorted(list(set(x)))
xp = {xp[i]:i for i in range(len(xp))}

print(*[xp[i] for i in x])