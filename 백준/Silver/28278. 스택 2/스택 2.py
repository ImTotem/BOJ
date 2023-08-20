import sys
input = lambda:sys.stdin.readline().strip()

stack = []
for _ in range(int(input())):
    cmd = input().split()
    
    if cmd[0] == '1':
        stack.append(cmd[1])
    elif cmd[0] == '2':
        print(stack.pop() if stack else -1)
    elif cmd[0] == '3':
        print(len(stack))
    elif cmd[0] == '4':
        print(int(not stack))
    else:
        print(stack[-1] if stack else -1)