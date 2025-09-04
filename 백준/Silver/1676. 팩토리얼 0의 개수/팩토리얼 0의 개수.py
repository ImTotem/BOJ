import sys
input = lambda: sys.stdin.readline().strip()
from math import factorial as facto

INF = float('inf')

def main():
    n = int(input())
    n = str(facto(n))[::-1]
    ans = 0
    for i in range(len(n)):
        if n[i] != '0': break
        ans += 1
    
    return ans
    
    
if __name__ == "__main__":
    print(main())
