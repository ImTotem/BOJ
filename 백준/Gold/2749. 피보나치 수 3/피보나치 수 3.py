n = int(input())

p = 1500000
fib = [0] * p
fib[1] = 1

for i in range(2, p):
    fib[i] = fib[i-1] + fib[i-2]
    fib[i] %= 1000000

print(fib[n%p])