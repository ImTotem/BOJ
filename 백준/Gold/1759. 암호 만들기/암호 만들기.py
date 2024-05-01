import sys
input = lambda:sys.stdin.readline().strip()

AEIOU = set("aeiou")

def main():
    l, c = map(int, input().split())
    chars = sorted(input().split())
    
    ans = []
    
    stack = []
    def dfs(nxt):
        s = set(stack)

        if len(stack) == l:
            if 2 <= len(s - AEIOU) and 1 <= len(s & AEIOU):
                ans.append(''.join(stack))
            return

        for i in range(nxt, c):
            stack.append(chars[i])
            dfs(i+1)
            stack.pop()

    dfs(0)

    return '\n'.join(ans)

print(main())