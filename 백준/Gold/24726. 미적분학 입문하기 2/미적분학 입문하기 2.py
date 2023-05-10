from math import pi
import sys

input = lambda: sys.stdin.readline().strip()

x1, y1, x2, y2, x3, y3 = map(int, input().split())

sort = lambda a, b, c: sorted([a, b, c], key = lambda x:x[0])

v = lambda a, b: (1/3)*(b[0]-a[0])*((a[1]+b[1])**2 - a[1]*b[1])

get_answer = lambda l, m, r: pi * abs( v(l, m) + v(m, r) - v(l, r) )

print(get_answer(*sort((x1, y1), (x2, y2), (x3, y3))), get_answer(*sort((y1, x1), (y2, x2), (y3, x3))))