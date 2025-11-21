import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque, defaultdict
from string import ascii_lowercase, ascii_uppercase

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    h, w = map(int, input().split())
    graph = [list('.' + input() + '.') for _ in range(h)]
    graph = [list('.' * (w+2))] + graph + [list('.' * (w+2))]
    keys = set(input())

    ans = 0
    q = deque([(0, 0)])
    doors = defaultdict(list)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + D[i], y + D[i+1]

            if not (0 <= nx < w+2 and 0 <= ny < h+2): continue
            if graph[ny][nx] == '*': continue

            if graph[ny][nx] in ascii_uppercase and graph[ny][nx].lower() not in keys:
                doors[graph[ny][nx]].append((nx, ny))
                continue
            
            if graph[ny][nx] in ascii_lowercase:
                if graph[ny][nx] not in keys:
                    q.extend(doors[graph[ny][nx].upper()])
                keys.add(graph[ny][nx])
            elif graph[ny][nx] == '$': ans += 1

            graph[ny][nx] = '*'
            q.append((nx, ny))

    return ans

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
