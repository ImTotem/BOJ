import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    t = [[] for _ in range(n+1)]
    
    max_height = 1
    while (1 << max_height) <= n:
        max_height += 1

    for _ in range(n-1):
        a, b = map(int, input().split())
        t[a].append(b)
        t[b].append(a)
    
    depth = [0] * (n+1)
    parent = [[0] * max_height for _ in range(n+1)]

    stack = [(1, 0)]
    
    while stack:
        node, prev = stack.pop()
        depth[node] = depth[prev] + 1
        parent[node][0] = prev
        
        for next_node in t[node]:
            if next_node != prev:
                stack.append((next_node, node))
    
    for k in range(1, max_height):
        for node in range(1, n+1):
            parent[node][k] = parent[parent[node][k-1]][k-1]

    def lca(a, b):
        if depth[a] > depth[b]:
            a, b = b, a
        
        diff = depth[b] - depth[a]
        for i in range(max_height):
            if diff & (1 << i):
                b = parent[b][i]
        
        if a == b:
            return a
        
        for i in range(max_height-1, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
        
        return parent[a][0]

    ans = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        ans.append(str(lca(a, b)))
    
    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
