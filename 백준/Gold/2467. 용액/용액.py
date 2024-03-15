import sys
input = lambda:sys.stdin.readline().strip()

from bisect import bisect_left

def main():
    n = int(input())
    sol = list(map(int, input().split()))

    ans = (sol[0], sol[1])
    for i in range(n):
        idx = min(n-1, bisect_left(sol, -sol[i]))
        
        if i != idx-1 and abs(sol[i]+sol[idx-1]) < abs(sum(ans)):
            ans = (sol[i], sol[idx-1])

        if i != idx and abs(sol[i]+sol[idx]) < abs(sum(ans)):
            ans = (sol[i], sol[idx])

    print(*sorted(ans))

main()