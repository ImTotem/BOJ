from sys import stdin
input = stdin.readline

while True:
    n = input()[:-1].lower()
    if n == '#': break

    print(sum(n.count(i) for i in "aeiou"))