import sys
input = lambda:sys.stdin.readline().strip()

def get_primes(n):
    is_prime = [False, False] + [True] * (n-1)
    ret = [0]
    
    for i in range(2, n+1):
        if is_prime[i]:
            ret.append(ret[-1] + i)
            for j in range(2*i, n+1, i): is_prime[j] = False

    return ret

def main():
    cnt = 0

    n = int(input())
    acc = get_primes(n)
    N = len(acc)
    
    l, r = 0, 1
    while r < N:
        cur = acc[r] - acc[l]
        if cur < n: r += 1
        elif n < cur: l += 1
        else:
            cnt += 1
            l += 1
            r += 1

    print(cnt)
main()