import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10**8)

INF = float('inf')

def main():
    n, m = map(int, input().split())
    parent = list(range(n + 1))


    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b: parent[a] = b

    def find(a):
        if a == parent[a]: return a
        parent[a] = find(parent[a])
        return parent[a]
    
    ans = []
    for _ in range(m):
        o, a, b = map(int, input().split())

        if o: ans.append(['NO', 'YES'][find(a) == find(b)])
        else: union(a, b)

    return '\n'.join(ans)
                
if __name__ == "__main__":
    print(main())
