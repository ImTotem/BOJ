import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n, _, _ = map(int, input().split())
    m, k = (list(map(int, input().split())) for _ in range(2))

    sqrt = int(n**.5)
    chk = [0] * (n+1)
    dummy = [0] * (sqrt+1)

    for i in m:
        chk[i] += 1
        dummy[i // sqrt] += 1
    
    for i in k:
        will = i + 1
        while dummy[will // sqrt] == 0 and will <= n:
            will = ((will // sqrt) + 1) * sqrt
        if will > n:
            will = 0
            while dummy[will // sqrt] == 0 and will <= n:
                will = ((will // sqrt) + 1) * sqrt

        while True:
            if chk[will] != 0:
                chk[will] -= 1
                dummy[will // sqrt] -= 1
                print(will)
                break
            will += 1


main()