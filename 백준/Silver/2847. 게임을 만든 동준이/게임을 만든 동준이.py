import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    n = int(input())
    lvls = [int(input()) for _ in range(n)]
    
    ans = 0
    for i in range(n-2, -1, -1):
        if lvls[i+1] <= lvls[i]:
            ans += lvls[i] - lvls[i+1] + 1
            lvls[i] = lvls[i+1] - 1
    
    return ans


if __name__ == "__main__":
    print(main())
