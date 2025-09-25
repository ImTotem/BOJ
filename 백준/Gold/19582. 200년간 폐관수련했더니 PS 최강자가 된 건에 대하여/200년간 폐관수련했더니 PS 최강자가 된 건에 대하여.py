import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    pc = tuple(tuple(map(int, input().split())) for _ in range(n))
    
    flag = False
    s, m = 0, 0
    for i in range(n):
        x, p = pc[i]
        m = max(m, p)
        if s > x:
            if flag: return 'Zzz'

            flag = True
            s -= p if s - m > x else m
        
        s += p
    
    return 'Kkeo-eok'

if __name__ == "__main__":
    print(main())
