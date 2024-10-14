import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    heights = [int(input()) for _ in range(n)]

    ans = 0

    stack = []
    for h in heights:
        while stack and stack[-1][0] < h:
            ans += stack.pop()[1]
        
        if not stack:
            stack.append((h, 1))
            continue

        if stack[-1][0] == h:
            cnt = stack.pop()[1]
            ans += cnt

            if stack: ans += 1
            stack.append((h, cnt+1))
        
        else:
            stack.append((h, 1))
            ans += 1
    
    return ans


if __name__ == "__main__": 
    print(main())
