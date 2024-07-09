import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())

    ans = 0
    for _ in range(n):
        word = input()

        stack = []
        for w in word:
            if stack and stack[-1] == w:
                stack.pop()
                continue

            stack.append(w)
        
        ans += not stack
    
    return ans

print(main())