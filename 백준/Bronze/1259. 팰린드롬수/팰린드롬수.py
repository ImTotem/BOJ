from sys import stdin
input = stdin.readline

while True:
    n = input()[:-1]
    if n == '0': break

    print("yes" if n == n[::-1] else "no")