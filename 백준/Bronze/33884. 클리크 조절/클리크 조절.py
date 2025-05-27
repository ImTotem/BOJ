import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    first = [tuple(map(int, input().split())) for _ in range(n)]
    second = [tuple(map(int, input().split())) for _ in range(n)]
    first.sort(); second.sort()
    x = second[0][0] - first[0][0]
    first.sort(key=lambda x:x[1]); second.sort(key=lambda x:x[1])
    y = second[0][1] - first[0][1]
    
    return f'{x} {y}'

if __name__ == "__main__":
    print(main())
