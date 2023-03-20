from sys import stdin
input = stdin.readline

stack = []

def push(x):
    global stack
    stack.append(x)

def pop():
    global stack
    print(stack.pop()) if len(stack) > 0 else print(-1)

def size():
    global stack
    print(len(stack))

def empty():
    global stack
    print(1) if len(stack) == 0 else print(0)

def top():
    global stack
    print(stack[-1]) if len(stack) > 0 else print(-1)

n = int(input())

for _ in range(n):
    cmd = input().split()
    
    if cmd[0] != "push":
        globals()[cmd[0]]()
    else:
        globals()[cmd[0]](cmd[1])
