from sys import stdin
input = stdin.readline

M = int(input())

s = 0b00000000000000000000

for i in range(M):
    c = input().split()

    if c[0] == "add":
        s |= (1 << int(c[1]))
    elif c[0] == "remove":
        s &= ~(1 << int(c[1]))
    elif c[0] == "check":
        print(1 if s & (1 << int(c[1])) != 0 else 0)
    elif c[0] == "toggle":
        s ^= (1 << int(c[1]))
    elif c[0] == "all":
        s = (1 << 21) - 1
    else:
        s = 0