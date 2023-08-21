import sys
input = lambda:sys.stdin.readline().strip()

s = set()
for _ in range(int(input())):
    a = set(input().split())
    if "ChongChong" in a or len(s&a):
        s.update(a)

print(len(s))