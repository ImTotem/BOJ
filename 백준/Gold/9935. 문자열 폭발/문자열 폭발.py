from sys import stdin
input = stdin.readline

string = input().strip()
bomb = list(input().strip())

string_length = len(string)
bomb_length = len(bomb)

stack = []

for i in range(string_length):
    stack.append(string[i])
    if stack[-bomb_length:] == bomb:
        for _ in range(bomb_length):
            stack.pop()

print(''.join(stack) if stack else "FRULA")