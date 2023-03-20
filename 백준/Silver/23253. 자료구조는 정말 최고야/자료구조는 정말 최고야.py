from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

flag = True

for _ in range(m):
    int(input())
    pile = list(map(int, input().split()))
    if sorted(pile) != pile[::-1]:
        flag = False

print("Yes" if flag else "No")