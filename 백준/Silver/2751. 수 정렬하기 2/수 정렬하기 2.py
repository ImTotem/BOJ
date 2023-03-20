from sys import stdin
input = stdin.readline

n = int(input())

li = sorted([int(input()) for _ in range(n)])

for i in li:
    print(i)