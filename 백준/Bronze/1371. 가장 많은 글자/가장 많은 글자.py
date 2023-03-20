from sys import stdin
input = stdin.readlines

lines = ''.join(input()).replace("\n", "").replace(" ", "")

a = list(set(lines))

max_ = 0
out = []
for i in a:
    cnt = lines.count(i)
    if cnt > max_:
        out = [i]
        max_ = cnt
    elif cnt == max_:
        out.append(i)

print(*sorted(out), sep="")