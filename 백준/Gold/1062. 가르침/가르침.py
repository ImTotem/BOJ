import sys
input = lambda: sys.stdin.readline().strip()
from string import ascii_lowercase
from itertools import combinations as combi

INF = float('inf')

def main():
    n, k = map(int, input().split())
    ws = [input().removeprefix('anta').removesuffix('tica') for _ in range(n)]
    for i in range(n):
        ws[i] = set(ws[i]) - set('antic')

    if k < 5: return 0
    k -= 5

    ans = 0
    
    for comb in combi(set(ascii_lowercase) - set('antic'), k):
        a = set(comb)
        cnt = 0
        for b in ws:
            cnt += b.issubset(a)
        
        ans = max(ans, cnt)

    return ans

if __name__ == "__main__":
    print(main())
