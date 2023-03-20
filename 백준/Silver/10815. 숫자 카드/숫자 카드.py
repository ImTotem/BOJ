from sys import stdin
input = stdin.readline

n = input()
ns = set(input().split())
m = input()
ms = input().split()

ans = [1 if i in ns else 0 for i in ms]

print(*ans)
