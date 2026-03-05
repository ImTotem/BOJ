import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque

INF = float('inf')
# D = [0, 1, 0, -1, 0]

D = {
    0: (0, -1),
    1: (0, 1),
    2: (-1, 0),
    3: (1, 0)
}

class Shark:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.dir = 0
        self.prior = [None] * 4

        self.ndir = 0
        self.nx = 0
        self.ny = 0
    
    def nxt(self, ndir, nx, ny):
        self.ndir = ndir
        self.nx = nx
        self.ny = ny
    
    def update(self):
        self.dir = self.ndir
        self.x = self.nx
        self.y = self.ny
    
    def __repr__(self):
        return f'{self.name}'

def main():
    n, m, k = map(int, input().split())
    graph = []
    sharks = dict()
    smells = defaultdict(lambda: deque())

    for y in range(n):
        graph.append(list(map(int, input().split())))
        for x in range(n):
            name = graph[y][x]
            if not name: continue
            sharks[name] = Shark(name, x, y)
            smells[name].append((x, y))
            graph[y][x] = sharks[name]

    for name, d in enumerate(map(int, input().split())):
        sharks[name + 1].dir = d - 1

    for i in range(m):
        for j in range(4):
            sharks[i + 1].prior[j] = list(map(lambda x:int(x) - 1, input().split()))
    
    def clear():
        for name in smells:
            if not smells[name]: continue
            x, y = smells[name].popleft()
            
            shark = graph[y][x]

            if (x, y) in smells[name]: continue

            if shark == 0:
                continue

            if shark.name not in sharks:
                graph[y][x] = 0

            if (shark.x, shark.y) != (x, y):
                graph[y][x] = 0
    
    def move(shark):
        for d in shark.prior[shark.dir]:
            nx, ny = shark.x + D[d][0], shark.y + D[d][1]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == 0:
                    shark.nxt(d, nx, ny)
                    return
        
        for d in shark.prior[shark.dir]:
            nx, ny = shark.x + D[d][0], shark.y + D[d][1]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] != 0 and graph[ny][nx].name == shark.name:
                    shark.nxt(d, nx, ny)
                    return

    for t in range(1, 1000 + 1):
        for shark in sharks.values():
            move(shark)
        
        delete = []
        for shark in sorted(sharks.values(), key=lambda x:x.name):
            cell = graph[shark.ny][shark.nx]
            if cell and cell.name < shark.name:
                delete.append(shark.name)
                continue
            
            shark.update()
            smells[shark.name].append((shark.x, shark.y))
            graph[shark.y][shark.x] = shark
        
        for name in delete:
            del sharks[name]
        
        if len(sharks) == 1:
            return t

        if t >= k: clear()

    return -1

if __name__ == "__main__":
    print(main())
