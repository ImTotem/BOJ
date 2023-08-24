import sys
input = lambda:sys.stdin.readline().strip()

R, C, T = map(int, input().split())

A = []
dust = 0
cleaner = None
for i in range(R):
    room = list(map(int, input().split()))

    A.append(room)
    dust += sum(room)

    if -1 in room:
        cleaner = (room.index(-1), i)
        dust += 1

d = [0, 1, 0, -1, 0]

def spreading():
    a = [i[:] for i in A]
    for y in range(R):
        for x in range(C):

            if A[y][x] in [-1, 0]:
                continue

            spread = 0
            for i in range(4):
                nx, ny = x+d[i], y+d[i+1]

                if 0 <= nx < C and 0 <= ny < R and A[ny][nx] != -1:
                    a[ny][nx] += A[y][x]//5
                    spread += 1
            
            a[y][x] -= (A[y][x]//5)*spread
    
    return a

def cleaning(x, y):
    global dust
    dust -= A[y-2][x]
    dust -= A[y+1][x]
    
    for i in range(y-2):
        A[y-2-i][x] = A[y-3-i][x]
    A[0] = A[0][1:]+[0]
    for i in range(y-1):
        A[i][-1] = A[i+1][-1]
    A[y-1] = [-1, 0]+A[y-1][1:-1]

    for i in range(R-y-2):
        A[y+1+i][x] = A[y+2+i][x]
    A[-1] = A[-1][1:]+[0]
    for i in range(R-y-1):
        A[-1-i][-1] = A[-2-i][-1]
    A[y] = [-1, 0]+A[y][1:-1]

for _ in range(T):
    A = spreading()

    cleaning(*cleaner)

print(dust)