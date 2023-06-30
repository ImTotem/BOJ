import sys
input = lambda:sys.stdin.readline().strip()

while -1 != (n:=int(input())):
    divisors = set()

    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            divisors.update([i, n//i])
    
    if sum(divisors) == 2*n:
        divisors = sorted(divisors)
        print(n, "=", end=' ')
        print(*divisors[:-1], sep=' + ')
    else:
        print(f"{n} is NOT perfect.")