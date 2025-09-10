import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    m = int(input())
    a = set(input().split()) if m else set()

    if n == 100: return 0

    channel = INF
    for i in range(1000001):
        if not (set(list(str(i))) & a):
            channel = min(channel, i, key=lambda x:abs(n - x))

    return min(len(str(channel)) + abs(n - channel), abs(n - 100))

    
if __name__ == "__main__":
    print(main())
