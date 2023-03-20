from sys import stdin
input = stdin.readline

atom = {"H": 1, "C": 12, "O": 16}

w = input().strip()

calc = 0
stack = []
for i in w:
    if i == "(":
        stack.append(i)
    elif i in "HCO":
        stack.append(atom[i])
    elif i == ")":
        temp = 0

        while True:
            target = stack.pop()
            
            if target == "(": break

            temp += target

        stack.append(temp)
    else:
        stack[-1] *= int(i)

print(sum(stack))