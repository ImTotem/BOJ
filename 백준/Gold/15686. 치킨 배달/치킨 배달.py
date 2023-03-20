INF = float("inf")
from sys import stdin
input = stdin.readline
from itertools import combinations as comb

N, M = map(int, input().split())

chicken = []
house = []

for y in range(N):
    in_ = list(map(int, input().split()))
    for x in range(N):
        if in_[x] == 1:
            house.append([x, y])
        elif in_[x] == 2:
            chicken.append([x, y])

len_c, len_h = len(chicken), len(house)

ans = INF
for c in comb(chicken, M):
    temp = 0
    for h in house:
        distance = INF
        for i in range(M):
            distance = min(distance, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
        temp += distance
    ans = min(ans, temp)

print(ans)