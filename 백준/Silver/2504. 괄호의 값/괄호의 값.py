from sys import stdin
input = stdin.readline

s = input().strip()

ans = 0

stack = []
temp = 1
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
        temp *= 2
    elif s[i] == "[":
        stack.append(s[i])
        temp *= 3
    elif s[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        elif s[i-1] == "(":
            ans += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        elif s[i-1] == "[":
            ans += temp
        stack.pop()
        temp //= 3

if stack:
    ans = 0

print(ans)