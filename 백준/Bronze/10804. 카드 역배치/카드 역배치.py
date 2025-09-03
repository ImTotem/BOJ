import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    ans = list(range(21))
    for _ in range(10):
        a, b = list(map(int, input().split()))
        
        ans[a:b+1] = ans[a:b+1][::-1]
    
    return ' '.join(str(ans[i]) for i in range(1, 21))


if __name__ == "__main__":
    print(main())
