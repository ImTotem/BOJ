from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())

queue = deque(list(range(1, n+1)))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])