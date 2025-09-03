import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    
    return '\n'.join(' '*i + '*'*(2*(n-i-1)+1) for i in range(n))


if __name__ == "__main__":
    print(main())
