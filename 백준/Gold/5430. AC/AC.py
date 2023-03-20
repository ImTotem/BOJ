from ast import literal_eval
from collections import deque
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    p = input()[:-1].replace("RR", "")
    n = int(input())
    d = deque(list(map(int, literal_eval(input()))))
    
    flag = True
    flag2 = True

    for i in p:
        if i == "R":
            flag = not flag
        else:
            if d:
                if flag:
                    d.popleft()
                else:
                    d.pop()
            else:
                print("error")
                flag2 = not flag2
                break
    
    if flag2:
        if not flag:
            print(str(list(reversed(d))).replace(' ', ''))
        else:
            print(str(list(d)).replace(' ', ''))