import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())

    ans = 0

    stack = []
    for _ in range(n):
        h = int(input())

        while stack and stack[-1] <= h:
            stack.pop()
        
        stack.append(h)
        ans += len(stack) - 1
    
    return ans

print(main())