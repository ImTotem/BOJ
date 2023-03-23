from collections import deque
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

queue = deque(list(range(1, n+1)))

result = []

for i in range(n-1):
    for j in range(k-1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))

result.append(str(queue.popleft()))

print(f"<{', '.join(result)}>")