import math

from sys import stdin

input = stdin.readline

S = input()[:-1]

setted = set(S)

chk = []

indexing = dict()

for i in setted:

    indexing[i] = [[0, 1][S[0]==i]]

for i in range(1, len(S)):

    for j in setted:

        indexing[j].append(indexing[j][i-1]+[0, 1][S[i]==j])

for _ in range(int(input())):

    a, l, r = [int(v) if 0 < i else v for i, v in enumerate(input().split())]

    if a in setted:

        print(indexing.get(a)[r] - indexing.get(a)[l] + [0, 1][S[l]==a])

    else:

        print(0)