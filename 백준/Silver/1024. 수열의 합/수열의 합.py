import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, l = map(int, input().split())

    for i in range(l, 101):
        s = n - (i * (i - 1)) // 2
        if s < 0: break
        if s % i == 0:
            res = s // i
            if res < 0: continue
            return ' '.join(str(res + j) for j in range(i))

    return -1
    
if __name__ == "__main__":
    print(main())
