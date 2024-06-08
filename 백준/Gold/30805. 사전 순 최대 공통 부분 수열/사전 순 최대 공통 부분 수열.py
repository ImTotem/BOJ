import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_set, b_set = set(a), set(b)
intersec = a_set & b_set
lcs = []
while intersec:
    num = max(intersec)
    lcs.append(num)
    ai, bi = a.index(num), b.index(num)
    del a[:ai+1]
    del b[:bi+1]
    a_set, b_set = set(a), set(b)
    intersec = a_set & b_set

print(len(lcs))
print(*lcs)
