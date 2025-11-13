import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n <= 10: return p[n]

    for _ in range(n - 10):
        p.append(p[-1] + p[-5])
    
    return p[n]
    

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
