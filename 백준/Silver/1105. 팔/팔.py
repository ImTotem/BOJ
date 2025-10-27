import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    l, r = map(int, input().split())
    ans = min(str(l).count('8'), str(r).count('8'))
    for i in range(l, r + 1):
        ans = min(ans, str(i).count('8'))
        if ans == 0: break
    
    return ans

if __name__ == "__main__":
    print(main())
