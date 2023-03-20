from sys import stdin
input = stdin.readline

n, m, b = map(int, input().split())
land = sum([list(map(int, input().split())) for _ in range(n)], [])

min_, max_ = min(land), max(land)

answer = [float("inf"), min_]
for base in range(min_, max_+1):
    get = 0
    put = 0
    for i in land:
        if i < base:
            put += base - i
        else:
            get += i - base
    
    if get + b >= put:
        t = get*2 + put
        answer = [t, base] if t <= answer[0] else answer


print(*answer)