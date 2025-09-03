import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    a = tuple(filter(lambda x:x%2, (int(input()) for _ in range(7))))
    return f'{sum(a)}\n{min(a)}' if a else -1


if __name__ == "__main__":
    print(main())
