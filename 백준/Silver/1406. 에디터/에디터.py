from sys import stdin
input = stdin.readline

n1 = list(input().rstrip())
n2 = []

for _ in range(int(input())):
    inp = input().split()
    cmd = inp[0]

    if cmd == "L":
        if n1:
            n2.append(n1.pop())
    elif cmd == "D":
        if n2:
            n1.append(n2.pop())
    elif cmd == "B":
        if n1:
            n1.pop()
    else:
        n1.append(inp[1])

print(''.join(n1+n2[::-1]))