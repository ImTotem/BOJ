from sys import stdin
input = stdin.readline

n = int(input())

tower = list(map(int, input().split()))

ans = []
stack = []
for i in range(n):
    while stack != []:
        if stack[-1][1] >= tower[i]:
            ans.append(stack[-1][0])
            stack.append((i+1, tower[i]))
            break
        else:
            stack.pop()
    
    if stack == []:
        ans.append(0)
        stack.append((i+1, tower[i]))

print(*[i for i in ans])
