import sys

input = lambda: sys.stdin.readline().strip()

infix = input()

stack = []
postfix = ""

for s in infix:
    if s.isalpha():
        postfix += s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                postfix += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                postfix+=stack.pop()
            stack.pop()

print(postfix + ''.join(stack[::-1]))