import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

def main():
    n = int(input())
    parent = list(map(int, input().split()))

    tree = defaultdict(set)
    
    for i in range(1, n):
        tree[parent[i]].add(i)
    
    def dfs(idx):
        if not tree[idx]: return 1
        w = len(tree[idx]) - 1
        a = sorted(dfs(child) for child in tree[idx])

        return max(a[i] + (w - i) for i in range(len(a))) + 1
    
    return dfs(0) - 1

if __name__ == "__main__":
    print(main())
