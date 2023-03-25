import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
filename = [input() for _ in range(n)]

pattern = list(filename[0])

for i in range(1, n):
    for j in range(len(filename[i])):
        if '?' != pattern[j] != filename[i][j]:
            pattern[j] = '?'

print(''.join(pattern))