import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    x = list(map(int, input().split()))

    S = set(x)

    ans = [0] * ((M:=max(S))+1)
    for i in x:
        if i == M: continue
        for j in range(2*i, M+1, i):
            if j in S:
                ans[i] += 1
                ans[j] -= 1
    
    print(*(ans[i] for i in x))

main()