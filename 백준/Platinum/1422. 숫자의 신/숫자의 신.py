import sys
input = lambda:sys.stdin.readline().strip()

from functools import cmp_to_key

def comp (a: str, b: str) -> int:
    return int(a + b) - int(b + a)


def main():
    k, n = map(int, input().split())
    cand = [input() for _ in range(k)]
    cand.extend([max(cand, key=int)] * (n - k))
    cand.sort(key=cmp_to_key(comp))

    ans = ''
    
    for i in range(n):
        ans = str(max(int(ans + cand[i]), int(cand[i] + ans)))

    return ans


if __name__ == "__main__":
    print(main())
