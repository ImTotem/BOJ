import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

word = [input() for _ in range(n)]

changed = dict()

for w in word:
    for j in range(length:=len(w)):
        add = 10**(length-j-1)
        changed[w[j]] = add if w[j] not in changed else changed[w[j]] + add

ans = 0

changed = sorted(changed.values(), reverse=True)
for i in range(len(changed)):
    ans += changed[i]*(9-i)

print(ans)