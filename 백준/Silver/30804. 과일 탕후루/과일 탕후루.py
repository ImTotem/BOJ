import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    s = list(map(int, input().split()))

    cnt = {}
    ans = 0

    l = 0
    for r in range(n):
        cnt[s[r]] = cnt[s[r]] + 1 if s[r] in cnt else 1
        
        while 2 < len(cnt):
            cnt[s[l]] -= 1
            if cnt[s[l]] == 0: cnt.pop(s[l])
            l += 1
        
        ans = max(ans, r - l + 1)
    
    return ans

print(main())