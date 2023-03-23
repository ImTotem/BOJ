from sys import stdin
input = stdin.readline

li = [0 for _ in range(10001)]

n = int(input())

for _ in range(n):
    li[int(input())] += 1

for i in range(1, 10001):
    cnt = li[i]
    
    if cnt != 0:
        for j in range(cnt):
            print(i)