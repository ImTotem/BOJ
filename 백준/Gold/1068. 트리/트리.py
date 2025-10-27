import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    x = int(input())

    tree = {i: set() for i in range(-1, n)}

    ans = 0

    for i in range(n):
        tree[parents[i]].add(i)
    
    tree[parents[x]].discard(x)
    stack = list(tree[-1])
    while stack:
        u = stack.pop()

        stack.extend(tree[u])

        ans += not tree[u]

    return ans

if __name__ == "__main__":
    print(main())