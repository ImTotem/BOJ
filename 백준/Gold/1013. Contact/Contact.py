import sys
import re

input = lambda: sys.stdin.readline().strip()

res = []

for _ in range(int(input())):
    string = input()
    p = re.compile("(100+1+|01)+")
    m = p.fullmatch(string)

    if m: res.append("YES")
    else: res.append("NO")

print(*res, sep="\n")