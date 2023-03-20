w, h, x, y, p = map(int, input().split())
r = h/2
cnt = 0

for _ in range(p):
    px, py = map(int, input().split())
    px -= x
    py -= y
    
    if 0 <= px and px <= w and 0 <= py and py <= h:
        cnt+=1
    elif w < px and (px-w)**2+(py-r)**2 <= r**2:
        cnt+=1
    elif px < 0 and px**2+(py-r)**2 <= r**2:
        cnt+=1

print(cnt)