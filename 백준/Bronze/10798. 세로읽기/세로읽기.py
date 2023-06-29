import sys
input = lambda:sys.stdin.readline().strip()

stack = [''] * 15
for _ in range(5):
    s = input()
    
    for i in range(len(s)):
        stack[i] += s[i]

print(''.join(stack))