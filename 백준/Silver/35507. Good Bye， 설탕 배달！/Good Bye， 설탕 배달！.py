import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')
D = [-1, 0, 1, 0, -1, -1, 1, 1, -1]

def main():
    n = int(input())
    prob = [list(map(int, input().split())) for _ in range(n)]

    a, b, c = 0, 0, 0
    for i, (ai, bi, ci, pi) in enumerate(prob):
        a, b, c = max(a, ai), max(b, bi), max(c, ci)
        
        if a + b + c + i + 1 > pi:
            return 'NO'
    
    return 'YES'


if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
