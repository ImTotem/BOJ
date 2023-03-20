from sys import stdin
import math
input = stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x = [x1, x2, x3]
y = [y1, y2, y3]

set_x = list(set(x))
set_y = list(set(y))

x_count = []
y_count = []
for i in range(2):
    x_count.append(x.count(set_x[i]))
    y_count.append(y.count(set_y[i]))

print(set_x[x_count.index(min(x_count))], set_y[y_count.index(min(y_count))])