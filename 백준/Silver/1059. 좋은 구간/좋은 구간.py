import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    l = int(input())
    s = [0] + sorted(map(int, input().split()))
    n = int(input())

    for i in range(l):
        if n <= s[i] or s[i+1] <= n: continue
        
        a, b = s[i] + 1, s[i+1] - 1
        return (n - a + 1) * (b - n + 1) - 1

    return 0

if __name__ == "__main__":
    print(main())
