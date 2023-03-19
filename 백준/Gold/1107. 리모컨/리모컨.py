from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
broken = set(map(int, input().split())) if 0 < M else set()

if N != 100:
    if M < 10:
        ansa, ansb = 0, 0
        a, b = N, N
        while True:
            if 0 <= a and set(map(int, list(str(a)))) & broken:
                a -= 1
                ansa += 1
            else:
                if a != -1:
                    print(min(abs(N-100), len(str(a)) + ansa))
                    break
                
            if set(map(int, list(str(b)))) & broken:
                b += 1
                ansb += 1
            else:
                print(min(abs(N-100), len(str(b)) + ansb))
                break
    else:
        print(abs(100-N))
else:
    print(0)