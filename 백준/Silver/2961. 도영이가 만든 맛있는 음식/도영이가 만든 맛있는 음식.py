import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    ing = [tuple(map(int, input().split())) for _ in range(n)]
    ans = INF
    
    def dfs(d, u, s, b):
        nonlocal ans
        if d == n:
            if u != 0: ans = min(ans, abs(s - b))
            return
        
        dfs(d+1, u, s, b)
        dfs(d+1, u+1, s*ing[d][0], b+ing[d][1])
    
    dfs(0, 0, 1, 0)

    return ans

if __name__ == "__main__":
    print(main())
