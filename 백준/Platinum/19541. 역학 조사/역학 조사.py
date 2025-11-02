import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    grps = [tuple(map(int, input().split())) for _ in range(m)]
    infected = [0] + list(map(int, input().split()))

    clear = set(i for i in range(1, n+1) if infected[i] == 0)

    ans = 'YES\n'
    for k, *ids in grps[::-1]:
        ids = set(ids)
        
        if not (clear & ids): continue
        
        clear |= ids
    
    ans += ' '.join('10'[i in clear] for i in range(1, n+1))
    
    sim = [int(not(i in clear)) for i in range(n+1)]
    sim[0] = 0
    for k, *ids in grps:
        ids = set(ids)
        if any(sim[i] for i in ids):
            for i in ids:
                sim[i] = 1

    if sim != infected: return 'NO'

    return ans


if __name__ == "__main__":
    print(main())
