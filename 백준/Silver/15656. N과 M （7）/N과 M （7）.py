import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = []

    stack = []
    def dfs():
        if len(stack) == m:
            ans.append(' '.join(stack))
            return
        
        for i in a:
            stack.append(str(i))
            dfs()
            stack.pop()
    
    dfs()

    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
