import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    a = [int(input(), 2) for _ in range(n)]
    b = [int(input(), 2) for _ in range(n)]

    ans = 0

    mat = [a[i] ^ b[i] for i in range(n)]
    for y in range(n - 2):
        for x in range(m - 2):
            if mat[y] & (1 << (m - x - 1)):
                ans += 1
                for i in range(3):
                    mat[y + i] ^= (0b111 << (m - x - 3))
    
    return ans if not sum(mat) else -1

if __name__ == "__main__":
    print(main())
