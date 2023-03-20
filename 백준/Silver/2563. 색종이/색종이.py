from sys import stdin
input = stdin.readline

n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

area = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            area += 1 if not paper[y+i][x+j] else 0
            paper[y+i][x+j] = 1

print(area)