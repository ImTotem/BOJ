from sys import stdin
input = stdin.readline

n = int(input())

sequence = [int(input()) for _ in range(n)]

stack = []
result = []

ans = ""

i = 1
index = 0
while len(result) < n:
    if sequence[index] in stack:
        if sequence[index] == stack[-1]:
            result.append(stack.pop())
            ans+="-"
            index+=1
        else:
            break
    else:
        stack.append(i)
        ans+="+"
        i+=1

if result == sequence:
    for i in ans:
        print(i)
else:
    print("NO")