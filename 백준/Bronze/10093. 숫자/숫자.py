import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    a, b = sorted(map(int, input().split()))
    cnt = max(b-a-1, 0)
    return f"{cnt}\n{' '.join(str(i) for i in range(a+1, b))}" if cnt else cnt


if __name__ == "__main__":
    print(main())
