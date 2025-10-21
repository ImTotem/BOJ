import sys
input = lambda:sys.stdin.readline().strip()

class Stack():
    def __init__(self): self.stack = []
    def push(self, n): self.stack.append(n)
    def pop(self): return self.stack.pop() if self.stack else -1
    def size(self): return len(self.stack)
    def empty(self): return int(not self.stack)
    def top(self): return self.stack[-1] if self.stack else -1

def main():
    stack = Stack()
    for _ in range(int(input())):
        cmd = input().split()
        op = cmd[0]
    
        if op == "push": stack.push(cmd[1])
        elif op == "pop": print(stack.pop())
        elif op == "size": print(stack.size())
        elif op == "empty": print(stack.empty())
        else: print(stack.top())

main()