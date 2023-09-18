import sys
input = lambda:sys.stdin.readline().strip()

n, m = map(int, input().split())

vtubers = dict()

for _ in range(n):
    name, day, start, end = input().split()
    start = list(map(int, start.split(":")))
    end = list(map(int, end.split(":")))
    
    week = (int(day)-1)//7

    times = (end[0]*60 + end[1]) - (start[0]*60 + start[1])

    if name not in vtubers:
        vtubers[name] = dict()

    if week not in vtubers[name]:
        vtubers[name][week] = [0, 0]

    vtubers[name][week][0] += 1
    vtubers[name][week][1] += times

ans = []
for name in vtubers:
    info = True
    if len(vtubers[name]) != m//7:
        info = False
    else:
        for week in vtubers[name]:
            if vtubers[name][week][0] < 5 or vtubers[name][week][1] < 3600:
                info = False
                break
            
    if info: ans.append(name)

ans.sort()

if ans: print(*ans, sep="\n")
else: print(-1)
