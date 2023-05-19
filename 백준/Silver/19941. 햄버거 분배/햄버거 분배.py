import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
placement = list(input())

answer = 0
for i in range(n):
    if placement[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if placement[j] == 'H':
                placement[j] = 0
                answer += 1
                break

print(answer)