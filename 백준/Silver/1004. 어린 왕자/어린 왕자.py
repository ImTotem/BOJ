from sys import stdin, setrecursionlimit
input = stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    cnt = 0

    for i in range(int(input())):
        cx, cy, r = map(int, input().split())
        a = ((cx-x1)**2+(cy-y1)**2)**(1/2)
        b = ((cx-x2)**2+(cy-y2)**2)**(1/2)

        if (a < r and b > r) or (a > r and b < r):
            cnt+=1
    print(cnt)