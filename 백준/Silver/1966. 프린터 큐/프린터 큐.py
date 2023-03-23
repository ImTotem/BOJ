from collections import deque
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    doc = deque(list(map(int, input().split())))

    targetPriority = doc[m]
    targetIndex = m

    cnt = 0
    while True:
        if max(doc) > targetPriority:
            if max(doc) != doc[0]:
                doc.append(doc.popleft())
            else:
                doc.popleft()
                cnt+=1
        else:
            if doc[0] < targetPriority:
                doc.append(doc.popleft())
            else:
                if targetIndex == 0:
                    cnt+=1
                    break
                else:
                    doc.popleft()
                    cnt+=1
                
        
        targetIndex = targetIndex-1 if targetIndex != 0 else n-cnt-1

    print(cnt)