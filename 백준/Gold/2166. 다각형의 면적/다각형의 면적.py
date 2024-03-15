import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())
    point = [tuple(map(float, input().split())) for _ in range(n)]
    point.append(point[0])

    ans = 0
    for i in range(n):
        ans += point[i][0]*point[i+1][1] - point[i][1]*point[i+1][0]

    print(round(abs(ans)/2, 1))

main()