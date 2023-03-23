from sys import stdin
input = stdin.readline

n = int(input())

a = list(map(int, input().split()))

nge = []

s = []

while len(nge) < n:
    if len(s) > 0:
        if a[-1] < s[-1]:
            nge.append(s[-1])
            s.append(a.pop())
        else:
            s.pop()
    else:
        nge.append(-1)
        s.append(a.pop())

print(*reversed(nge))