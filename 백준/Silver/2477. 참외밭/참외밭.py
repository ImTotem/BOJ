from collections import deque
from sys import stdin
input = stdin.readline

k = int(input())

vec = deque()
dis = deque()
for i in range(6):
    data = list(map(int, input().split()))
    vec.append(data[0])
    dis.append(data[1])

w1 = [vec.count(1), vec.count(2)].index(1)+1
h1 = [vec.count(3), vec.count(4)].index(1)+3

idx1 = vec.index(w1)
idx2 = vec.index(h1)

while max(idx1, idx2) != 1:
    vec.rotate(1)
    dis.rotate(1)

    idx1 = vec.index(w1)
    idx2 = vec.index(h1)

s = dis[vec.index(w1)]*dis[vec.index(h1)]

print((s-dis[3]*dis[-2])*k)