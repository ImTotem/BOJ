import sys
input = lambda:sys.stdin.readline().strip()

dx = {'u': 0, 'd': 0, 'l': -1, 'r': 1}
dy = {'u': -1, 'd': 1, 'l': 0, 'r': 0}

atk_dmg, atk_range, speed, req_xp, xp, lvl = 5, 1, 1, 10, 0, 1

act = 0
drug, overdose = 0, 0

py, px = 0, 0

n, m = map(int, input().split())
world = [list(input()) for _ in range(n)]

mons = dict()
k = int(input())
mh, md, mexp = (list(map(int, input().split())) for _ in range(3))

for y in range(n):
    for x in range(m):
        if world[y][x] == 'm': mons[(y, x)] = len(mons)
        elif world[y][x] == 'p': px, py = x, y

world[py][px] = '.'

def action(n):
    global act, overdose
    overdose -= min(overdose, n)
    act += n

def drugs(d):
    global drug, overdose, speed

    speed = max(0, speed - dy[d])
    action(2)
    if (drug:=(drug+1)%5) == 0: overdose = 10

def tp(d):
    global px, py

    ny, nx = py + dy[d]*speed, px + dx[d]*speed
    if not (0 <= ny < n and 0 <= nx < m): return
    if world[ny][nx] in '*m': return
    px, py = nx, ny
    action(1)

def exp():
    global xp, req_xp, lvl, atk_range, atk_dmg
    
    while (req_xp <= xp):
        xp -= req_xp
        atk_dmg += lvl
        lvl += 1
        atk_range += 1
        req_xp += 10
    
def attack(d):
    global xp
    action(3)
    
    for i in range(1, atk_range+1):
        ny, nx = py + dy[d]*i, px + dx[d]*i
        if not (0 <= ny < n and 0 <= nx < m): break
        if world[ny][nx] == '*': break
        if world[ny][nx] == 'm':
            idx = mons[(ny, nx)]
            mh[idx] -= max(0, atk_dmg - md[idx])

            if mh[idx] <= 0:
                world[ny][nx] = '.'
                xp += mexp[idx]
    
    exp()

input()
for cmd in input().split():
    if cmd in "udlr": tp(cmd)
    elif cmd == "w": action(1)
    elif overdose: continue
    elif cmd[0] == 'a': attack(cmd[1])
    elif cmd[0] == "d": drugs(cmd[1])
    elif world[py][px] == 'g': break

world[py][px] = 'p'

print(lvl, xp)
print(act)
for i in world: print(*i, sep="")
for i in mh: print(i) if 0<i else 0