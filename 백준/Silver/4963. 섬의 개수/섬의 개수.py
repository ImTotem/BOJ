import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')
D = [-1, 0, 1, 0, -1, -1, 1, 1, -1]

def main(w, h):
    graph = [list(map(int, input().split())) for _ in range(h)]

    ans = 0

    def dfs(x, y):
        if graph[y][x] == 0:
            return 0

        graph[y][x] = 0
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()

            for i in range(8):
                nx, ny = x + D[i], y + D[i + 1]
                
                if not (0 <= nx < w and 0 <= ny < h): continue
                if graph[ny][nx] == 0: continue
                
                graph[ny][nx] = 0
                stack.append((nx, ny))
        
        return 1
    
    for y in range(h):
        for x in range(w):
            ans += dfs(x, y)

    return ans


if __name__ == "__main__":
    w, h = map(int, input().split())
    while (w, h) != (0, 0):
        print(main(w, h))
        w, h = map(int, input().split())
