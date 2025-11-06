import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    ans = 0

    stack = []
    def dfs():
        nonlocal ans
        if len(stack) == n:
            ans += int(''.join(stack)) % 3 == 0
            return
        
        for i in '012':
            if not stack and i == '0': continue
            stack.append(i)
            dfs()
            stack.pop()
    
    dfs()

    return ans

if __name__ == "__main__":
    print(main())
