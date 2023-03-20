from sys import stdin
input = stdin.readline

n = int(input())

for _ in range(n):
    t = input().strip().replace("()", "")
    
    while t.count("()") > 0:
        t=t.replace("()", "")

    if len(t) > 0:
        print("NO")
    else:
        print("YES")
