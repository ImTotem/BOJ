from sys import stdin
input = stdin.readline

n = int(input())

li = []
for _ in range(n):
    mem = input().split()
    li.append((int(mem[0]), mem[1]))

li.sort(key=lambda x: x[0])

for i in li:
    print(i[0], i[1])
