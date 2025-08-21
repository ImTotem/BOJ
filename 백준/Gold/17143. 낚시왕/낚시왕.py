import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

class Entity:
    def __init__(self, r, c):
        self.r = r
        self.c = c

class Shark(Entity):
    def __init__(self, r, c, s, d, z, i):
        super().__init__(r, c)
        self.s = s  
        self.d = d
        self.z = z
        self.i = i
    
    def move(self, br, bc):
        pos, maxi = self.c, bc
        if self.d <= 2: pos, maxi = self.r, br
        if maxi == 1: return

        effs = self.s % (2 * (maxi - 1))
        d = pos - 1 if self.d in {2, 3} else 2 * maxi - pos - 1

        q, rem = divmod(d + effs, maxi - 1)
        
        npos = [rem + 1, maxi - rem][q % 2]

        if self.d <= 2: self.r = npos
        else: self.c = npos

        self.d = ((1, 2), (4, 3))[self.d > 2][1 - q % 2]
    
    def __lt__(self, o):
        return self.z < o.z
    
    def __le__(self, o):
        return self.z <= o.z
    
    def __hash__(self):
        return hash(self.i)

class FishingKing(Entity):
    def __init__(self):
        super().__init__(0, 0)
        self.score = 0
    
    def move(self):
        self.c += 1

def main():
    r, c, m = map(int, input().split())
    sharks = {Shark(*map(int, input().split()), i) for i in range(m)}
    king = FishingKing()

    board = [[[] for _ in range(c+1)] for _ in range(r+1)]
    for shark in sharks:
        board[shark.r][shark.c].append(shark)

    def fishing():
        for i in range(1, r+1):
            if len(board[i][king.c]) > 0:
                king.score += board[i][king.c][0].z
                sharks.discard(board[i][king.c][0])
                board[i][king.c].pop()
                break
    
    def sharks_move():
        for shark in sharks:
            board[shark.r][shark.c].remove(shark)
            shark.move(r, c)
            board[shark.r][shark.c].append(shark)

        eaten = set()
        for shark in sharks:
            board[shark.r][shark.c].sort(reverse=True)
            while len(board[shark.r][shark.c]) > 1:
                eaten.add(board[shark.r][shark.c].pop())
        
        for shark in eaten:
            sharks.discard(shark)

    while king.c < c:
        king.move()
        fishing()
        sharks_move()
    
    return king.score

if __name__ == "__main__":
    print(main())
