import sys
input = lambda:sys.stdin.readline().strip()

class Stack:
    def __init__(self): self.list = []
        
    def push(self, num): self.list.append(num)
    
    def pop(self):
        if not self.list: return -1
        return self.list.pop()
        
    def size(self): return len(self.list)
        
    def empty(self): return int(not len(self.list))
        
    def top(self): return self.list[-1] if self.list else -1

stack = Stack()
for _ in range(int(input())):
    cmd = input().split()
    op = cmd[0]
 
    if op == "push": stack.push(cmd[1])
    elif op == "pop": print(stack.pop())
    elif op == "size": print(stack.size())
    elif op == "empty": print(stack.empty())
    else: print(stack.top())