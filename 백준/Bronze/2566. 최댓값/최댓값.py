from sys import stdin
input = stdin.readline

max_ = 0
x, y = 0, 0
for i in range(9):
    col = list(map(int, input().split()))
    if max(col) > max_:
        max_ = max(col)
        x = col.index(max_)
        y = i

print(max_)
print(y+1, x+1)