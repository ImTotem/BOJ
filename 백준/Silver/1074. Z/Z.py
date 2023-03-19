N, r, c = map(int, input().split())

ans = 0
for i in range(N):
    n = 2**(N-i-1)
    if n <= c and r < n:
        ans += n**2
        c -= n
    elif c < n and n <= r:
        ans += 2*n**2
        r -= n
    elif n <= c and n <= r:
        ans += 3*n**2
        r -= n
        c -= n

print(ans)