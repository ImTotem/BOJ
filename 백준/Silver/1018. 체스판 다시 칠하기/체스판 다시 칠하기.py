import sys
input = lambda: sys.stdin.readline().strip()
from collections import Counter

INF = float('inf')

def main():
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]

    ans = INF
    
    for i in range(n - 7):
        for j in range(m - 7):
            a, b = 0, 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    a += board[k][l] != "WB"[(k+l)%2]
                    b += board[k][l] != "BW"[(k+l)%2]
            
            ans = min(ans, a, b)
    
    return ans

    
if __name__ == "__main__":
    print(main())
