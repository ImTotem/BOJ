from sys import stdin
import math
input = stdin.readline

N = int(input())
start = 1

i=1
while start < N:
    i+=1
    start+=i

pos = []
if i % 2 == 0:
    pos = [i, 1]
else:
    pos = [1, i]

for j in range(N-(start-i)-1):
    if i % 2 == 0:
        pos = [pos[0]-1, pos[1]+1]
    else:
        pos = [pos[0]+1, pos[1]-1]

print(f"{pos[1]}/{pos[0]}")