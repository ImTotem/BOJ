import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict

INF = float('inf')

def main():
    parent = defaultdict(lambda: ['', 0])

    def union(a, b):
        a, b = find(a), find(b)

        if a != b:
            if parent[a][1] < parent[b][1]: a, b = b, a
            parent[a][1] += parent[b][1]
            parent[b][0] = a

        return parent[a][1]
    
    def find(x):
        if not parent[x][0]:
            parent[x] = [x, 1]
            return x
        if x == parent[x][0]: return x
        parent[x][0] = find(parent[x][0])
        return parent[x][0]
    
    ans = []
    for _ in range(int(input())):
        a, b = input().split()
        ans.append(str(union(a, b)))
    
    return '\n'.join(ans)
    
if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
