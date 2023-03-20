from collections import deque
from sys import stdin
input = stdin.readline

queue = deque()

def push(x):
    queue.append(x)

def pop():
    return queue.popleft() if queue else -1

def size():
    return len(queue)

def empty():
    return 0 if queue else 1

def front():
    return queue[0] if queue else -1

def back():
    return queue[-1] if queue else -1

for i in range(int(input())):
    command = input()[:-1].split()

    cmd = command[0]
    if cmd == "push":
        push(command[1])
    elif cmd == "pop":
        print(pop())
    elif cmd == "size":
        print(size())
    elif cmd == "empty":
        print(empty())
    elif cmd == "front":
        print(front())
    elif cmd == "back":
        print(back())