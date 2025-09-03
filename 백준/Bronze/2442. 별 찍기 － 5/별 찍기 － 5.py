import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    
    return '\n'.join(' '*(n - i - 1) + '*'*(2*i+1) for i in range(n))


if __name__ == "__main__":
    print(main())
