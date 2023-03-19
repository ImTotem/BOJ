from sys import stdin
input = stdin.readline

n = int(input())

points = [input().replace("\n", "") for _ in range(n)]

points = sorted(list(set(points)), key=lambda x:(len(x), x))

for i in points:
    print(i)