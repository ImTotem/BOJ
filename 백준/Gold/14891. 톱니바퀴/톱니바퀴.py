import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

INF = float('inf')

def main():
    gs = [[None]] + [deque(map(int, list(input()))) for _ in range(4)]

    for _ in range(int(input())):
        rot = deque([tuple(map(int, input().split()))])
        
        visited = [0] * 5
        visited[rot[0][0]] = 1
        while rot:
            n, d = rot.popleft()

            if 0 < n - 1 and not visited[n - 1] and gs[n][6] != gs[n - 1][2]:
                rot.append((n - 1, -d))
                visited[n - 1] = 1
            
            if n + 1 < 5 and not visited[n + 1] and gs[n][2] != gs[n + 1][6]:
                rot.append((n + 1, -d)) 
                visited[n + 1] = 1

            gs[n].rotate(d)
    
    return sum(2**i if gs[i+1][0] else 0 for i in range(4))


if __name__ == "__main__":
    print(main())
