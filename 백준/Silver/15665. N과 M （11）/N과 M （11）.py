import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = set()

    stack = []
    def dfs():
        if len(stack) == m:
            ans.add(tuple(stack))
            return
        
        for i in a:
            stack.append(i)
            dfs()
            stack.pop()
    
    dfs()

    return '\n'.join(' '.join(map(str, s)) for s in sorted(ans))

if __name__ == "__main__":
    print(main())
