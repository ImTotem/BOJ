import sys
input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush

INF = float('inf')

def main():
    l, c = map(int, input().split())
    chars = list(input().split())
    chars.sort()

    aeiou = set('aeiou')
    consonant = set(chars) - aeiou
    
    ans = []

    stack = []
    def dfs(nxt):
        s = set(stack)

        if len(stack) == l:
            if len(s & consonant) >= 2 and len(s & aeiou) >= 1:
                ans.append(''.join(stack))
            return
        
        for i in range(nxt, c):
            stack.append(chars[i])
            dfs(i + 1)
            stack.pop()
    
    dfs(0)

    return '\n'.join(ans)

    return
    
if __name__ == "__main__":
    print(main())
