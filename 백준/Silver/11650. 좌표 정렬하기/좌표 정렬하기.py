from sys import stdin
input = stdin.readline

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

points.sort()

for i in points:
    print(f"{i[0]} {i[1]}")