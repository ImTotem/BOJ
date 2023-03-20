from sys import stdin
input = stdin.readline

while True:
    f, s = map(int, input().split())
    if [f,s] == [0,0]:break

    if s % f == 0:
        print("factor")
    elif f % s == 0:
        print("multiple")
    else:
        print("neither")