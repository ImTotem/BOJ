import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

def main():
    s = input()

    left = deque()
    right = deque()

    for c in s:
        if c == "<":
            if left: right.appendleft(left.pop())
        elif c == ">":
            if right: left.append(right.popleft())
        elif c == "-":
            if left: left.pop()
        else:
            left.append(c)
    
    return ''.join(left + right)

for _ in range(int(input())):
    print(main())