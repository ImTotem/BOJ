from sys import stdin
input = stdin.readline

x = int(input())

stick = 64
min_ = 64
cnt = 1

while stick > x:
    min_ = min_ // 2
    if stick - min_ >= x:
        stick -= min_
    else:
        cnt+=1

print(cnt)