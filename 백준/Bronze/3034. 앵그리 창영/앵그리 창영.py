from sys import stdin
input = stdin.readline

n, w, h = map(int, input().split())
hypot = (w**2+h**2)**(0.5)

for i in range(n):
    m = int(input())

    if m <= w or m <= h or m <= hypot:
        print("DA")
    else:
        print("NE")
