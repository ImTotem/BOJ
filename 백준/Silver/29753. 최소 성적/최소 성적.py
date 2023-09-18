import sys
input = lambda:sys.stdin.readline().strip()

n, x = input().split()
n, x = (int(n), float(x))

mapper = {"A+": 4.5, "A0": 4, "B+": 3.5, "B0": 3, "C+": 2.5, "C0": 2, "D+": 1.5, "D0": 1, "F": 0}

s1 = 0
s2 = 0
for _ in range(n-1):
    c, g = input().split()
    c = int(c)

    s1 += c*mapper[g]
    s2 += c

l = int(input())

s2 += l

ans = "impossible"
for m in mapper:
    score = (s1+(l*mapper[m])) / s2
    tmp = str(score).split('.')
    score = float(f"{tmp[0]}.{tmp[1][:2]}")

    if x < score:
        ans = m

print(ans)