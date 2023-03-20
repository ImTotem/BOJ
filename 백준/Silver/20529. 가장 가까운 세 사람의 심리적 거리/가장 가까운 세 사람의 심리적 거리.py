import math
from sys import stdin
input = stdin.readline

def comp(a, b):
    point = 0
    for i in range(4):
        if a[i] != b[i]:
            point+=1
    return point

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().split()

    if n > 48:
        print(0)
    else:
        _set = list(set(mbti))
        _map = [[comp(_set[a], _set[b]), _set[a], _set[b]] for a in range(len(_set)) for b in range(a+1, len(_set)) for _ in range(mbti.count(_set[a])*mbti.count(_set[b]))]
        _map+=[[0, i, i] for i in _set if mbti.count(i) > 1 for _ in range(math.comb(mbti.count(i),2))]
        
        cnt=13
        sel = []
        for i in _set:

            target = sorted([j for j in _map if i in j])[:2]
            
            targetPoint = target[0][0]+target[1][0]
            
            targetMbti = list(target[0][1:]+target[1][1:])
            targetMbti.remove(i)
            targetMbti.remove(i)
            targetPoint += [i for i in _map if targetMbti[0] in i and targetMbti[1] in i][0][0]

            if targetPoint < cnt:
                cnt = targetPoint
                sel = targetMbti

        print(cnt)