import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(2000)

INF = float('inf')
D = [-1, 0, 1, 0, -1, -1, 1, 1, -1]

def main():
    m = int(input())
    bags = list(map(int, input().split()))
    n = int(input())
    items = list(map(int, input().split()))

    while len(items) < n:
        row = input()
        if not row:
            break
        items.extend(list(map(int, row.split())))
        
    if not items or n == 0:
        return 0
        
    items.sort()
    
    bags = [b for b in bags if b >= items[0]]
    m = len(bags)
    if m == 0:
        return 0
        
    bags.sort()
    
    total = sum(bags)
    
    psum = [0] * n
    psum[0] = items[0]
    for i in range(1, n):
        psum[i] = psum[i-1] + items[i]
        
    limit = 0
    for i in range(n):
        if psum[i] <= total:
            limit = i + 1
        else:
            break

    temp = [0] * m
    steps = 0

    def dfs(idx, start, waste, allow):
        nonlocal steps
        steps += 1
        
        if steps > 50000:
            return False
            
        if idx < 0:
            return True
            
        item = items[idx]
        base = items[0]
        same = (idx > 0 and items[idx-1] == item)
        
        seen = []
        sadd = seen.append
        
        for j in range(start, m):
            tj = temp[j]
            if tj < item or tj in seen:
                continue
                
            if tj == item:
                temp[j] = 0
                nxt = j if same else 0
                if dfs(idx - 1, nxt, waste, allow):
                    return True
                temp[j] = tj
                break
                
            sadd(tj)
            
            rem = tj - item
            nw = waste
            if rem < base:
                nw += rem
                
            if nw <= allow:
                temp[j] = rem
                nxt = j if same else 0
                if dfs(idx - 1, nxt, nw, allow):
                    return True
                temp[j] = tj
                
        return False

    def check(k):
        nonlocal steps
        if k == 0:
            return True
            
        allow = total - psum[k-1]
        temp[:] = bags[:]
        steps = 0
        return dfs(k - 1, 0, 0, allow)

    def bfd(k):
        clone = bags[:]
        for i in range(k - 1, -1, -1):
            pick = -1
            gap = INF
            for j in range(m):
                if clone[j] >= items[i]:
                    d = clone[j] - items[i]
                    if d < gap:
                        gap = d
                        pick = j
                        if gap == 0:
                            break
            if pick != -1:
                clone[pick] -= items[i]
            else:
                return False
        return True

    ans = 0
    low = 0
    high = limit
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid == 0:
            low = mid + 1
            continue
            
        if items[mid-1] > bags[-1]:
            high = mid - 1
            continue
            
        if bfd(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    left = ans + 1
    right = limit
    
    while left <= right:
        mid = (left + right) // 2
        
        if items[mid-1] > bags[-1]:
            right = mid - 1
            continue
            
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return ans

if __name__ == "__main__":
    print(main())
