import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

INF = float('inf')

def main():
    n = int(input())
    c = sorted(map(int, input().split()))
    m = int(input())
    b = sorted(map(int, input().split()))

    if c[-1] < b[-1]: return -1

    ans = 0
    
    while b:
        later = []
        for i in range(n):
            while b and c[n - i - 1] < b[-1]:
                later.append(b.pop())
            
            if b: b.pop()
        
        b += later[::-1]

        ans += 1
        
    return ans
    

if __name__ == "__main__":
    print(main())
