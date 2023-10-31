import sys
input = lambda:sys.stdin.readline().strip()

def main():
    stack = []
    for _ in range(int(input())):
        cmd = input().split()
        op = cmd[0]
    
        if op == "push": stack.append(cmd[1])
        elif op == "pop": print(stack.pop() if stack else -1)
        elif op == "size": print(len(stack))
        elif op == "empty": print(int(not stack))
        else: print(stack[-1] if stack else -1)

main()