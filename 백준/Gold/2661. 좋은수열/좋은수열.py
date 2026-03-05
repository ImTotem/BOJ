import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n = int(input())
    
    def dfs(ans):
        
        if len(ans) == n:
            return ''.join(ans)
        
        for i in '123':
            nxt = ans + i

            for j in range(1, len(nxt) // 2 + 1):
                if nxt[-j:] == nxt[-2*j:-j]:
                    break

            else:
                ret = dfs(nxt)
                if ret and len(ret) == n:
                    return ret
    
    return dfs('')

if __name__ == "__main__":
    print(main())
