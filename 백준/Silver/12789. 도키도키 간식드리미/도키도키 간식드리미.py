import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

n = int(input())
que = deque(map(int, (input()+' 0 0').split()))

stack = [0]

cnt = 1
while que[0] or stack[-1]:
    if que[0] == cnt:
        cnt += 1
        que.popleft()
        continue
    
    if stack[-1] == cnt:
        cnt += 1
        stack.pop()
        continue
    
    stack.append(que.popleft())

print(["Sad", "Nice"][n+1==cnt])