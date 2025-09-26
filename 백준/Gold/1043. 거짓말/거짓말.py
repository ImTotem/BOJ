import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    r, *a = map(int, input().split())
    a = set(a)
    ps = [set(list(map(int, input().split()))[1:]) for _ in range(m)]

    if not r: return m

    while ps:
        flag = True
        for b in ps:
            if a & b:
                a |= b
                ps.remove(b)
                m -= 1
                flag = False
        
        if flag: return m
    
    return m

if __name__ == "__main__":
    print(main())
