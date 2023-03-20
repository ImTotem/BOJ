from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    print("NO BRAINS" if x < y else "MMM BRAINS")