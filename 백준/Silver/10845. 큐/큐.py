from collections import deque
from sys import stdin
input = stdin.readline

que = deque()
for i in range(int(input())):
    inp = input()[:-1].split()
    cmd = inp[0]
    if cmd == "push":
        que.append(inp[1])
    elif cmd == "pop":
        print(que.popleft() if que else -1)
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        print(0 if que else 1)
    elif cmd == "front":
        print(que[0] if que else -1)
    else:
        print(que[-1] if que else -1)