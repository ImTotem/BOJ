from sys import stdin
input = stdin.readline

l, p = map(int, input().split())
print(*[i-l*p for i in map(int, input().split())])