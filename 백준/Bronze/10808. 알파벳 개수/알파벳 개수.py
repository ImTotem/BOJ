import sys
input = lambda: sys.stdin.readline().strip()
from collections import Counter
from string import ascii_lowercase

INF = float('inf')

def main():
    s = input()
    cnt = Counter(s)
    return ' '.join(str(cnt[i]) for i in ascii_lowercase)


if __name__ == "__main__":
    print(main())
