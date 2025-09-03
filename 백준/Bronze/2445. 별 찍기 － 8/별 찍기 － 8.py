import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    
    ans = ['*' * (i + 1) + ' ' * (2 * (n - i - 1)) + '*' * (i + 1) for i in range(n)]
    ans.extend(ans[:n-1][::-1])
    
    return '\n'.join(ans)


if __name__ == "__main__":
    print(main())
