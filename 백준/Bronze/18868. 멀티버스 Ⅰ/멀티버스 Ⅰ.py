from sys import stdin
input = stdin.readline

M, N = map(int, input().split())
universes = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    temp = sorted(set(universes[i]))

    idx = [temp.index(j) for j in universes[i]]

    universes[i] = idx

ans = 0
for i in range(M):
    for j in range(i+1, M):
        if universes[i] == universes[j]:
            ans += 1

print(ans)