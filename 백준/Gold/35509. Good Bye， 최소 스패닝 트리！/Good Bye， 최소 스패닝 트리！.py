def main():
    n, m = map(int, input().split())
    
    graph = []
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((w, u, v, i + 1))
    
    graph.sort(key=lambda x: x[0])

    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    def union(a, b):
        a, b = find(a), find(b)
        a, b = (b, a) if rank[a] > rank[b] else (a, b)
        
        parent[a] = b
        rank[b] += 1
    
    def find(x):
        if x == parent[x]: return x
        parent[x] = find(parent[x])
        return parent[x]

    mst_w = 0
    max_w = 0
    cnt = 0
    
    for w, u, v, idx in graph:
        ru, rv = find(u), find(v)
        if ru != rv:
            union(ru, rv)
            mst_w += w
            max_w = max(max_w, w)
            cnt += 1
            if cnt == n - 1: break

    graph = [e for e in graph if e[0] <= max_w]
    graph.sort(key=lambda x: x[0], reverse=True)

    parent = list(range(n + 1))
    mbst_w = 0
    res = []
    cnt = 0
    
    for w, u, v, idx in graph:
        ru, rv = find(u), find(v)
        if ru != rv:
            union(ru, rv)
            mbst_w += w
            res.append(str(idx))
            cnt += 1
            if cnt == n - 1: break

    ans = ['NO']

    if mbst_w > mst_w:
        ans.append('YES')
        ans.extend(res)
    else:
        ans.append('NO')

    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
