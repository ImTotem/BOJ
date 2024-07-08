import sys
input = lambda:sys.stdin.readline().strip()

def main():
    brackets = input().replace("()", "L")

    stack = []

    ans = 0
    for b in brackets:
        if b == 'L':
            ans += len(stack)
        elif b == ')':
            ans += 1
            stack.pop()
        else:
            stack.append(b)
    
    return ans

print(main())