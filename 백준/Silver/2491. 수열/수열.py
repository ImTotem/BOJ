import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    a = tuple(map(int, input().split()))

    ans = 1
    
    a1, a2 = 1, 1
    for i in range(n-1):
        if a[i] <= a[i+1]: a1 += 1
        else:
            ans = max(ans, a1)
            a1 = 1
        
        if a[i+1] <= a[i]: a2 += 1
        else:
            ans = max(ans, a2)
            a2 = 1
    
    print(max(ans, a1, a2))

main()