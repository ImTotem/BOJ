import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')
D = [-1, 0, 1, 0, -1, -1, 1, 1, -1]

def main():
    n = int(input())
    
    ans = ['' for _ in range(2 * n)]
    for i in range(2 * n):
        ans[i] += ' ' * (2 * n - 1 - i) + '*'
        
        if i < n:
            a, b, c = n, 2 * i + 1, n - 1 - i
        else:
            a, b, c = 2 * i - n + 1, 4 * n - 2 * i - 1, i - n
            
        ans[i] += ' ' * a + '*' + ' ' * b + '*' + ' ' * c
    
    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
