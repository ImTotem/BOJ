import sys

input = lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    a, b = map(int, input().split())
    s = [a%10]

    while (s[-1]*a)%10 not in s:
        s.append((s[-1]*a)%10)
    
    ans = s[b%len(s)-1]

    print(ans if ans else 10)