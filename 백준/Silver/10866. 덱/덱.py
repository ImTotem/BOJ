from collections import deque
from sys import stdin
input = stdin.readline

d = deque()

for _ in range(int(input())):
    command = input()[:-1].split()

    cmd = command[0]
    if cmd == "push_front":
        d.appendleft(command[1])
    elif cmd == "push_back":
        d.append(command[1])
    elif cmd == "pop_front":
        print(d.popleft() if d else -1)
    elif cmd == "pop_back":
        print(d.pop() if d else -1)
    elif cmd == "size":
        print(len(d))
    elif cmd == "empty":
        print(0 if d else 1)
    elif cmd == "front":
        print(d[0] if d else -1)
    elif cmd == "back":
        print(d[-1] if d else -1)