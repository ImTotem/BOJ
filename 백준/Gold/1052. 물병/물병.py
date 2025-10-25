import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, k = map(int, input().split())
    
    def rem(n, x):
        if n == 0 or x == 0: return n

        nxt = n & ~(1 << (n.bit_length() - 1))

        return rem(nxt, x - 1)
    
    if k >= n.bit_count(): return 0

    ans = rem(n, k - 1)
    return (ans ^ ((1 << ans.bit_length()) - 1)) + 1

if __name__ == "__main__":
    print(main())
