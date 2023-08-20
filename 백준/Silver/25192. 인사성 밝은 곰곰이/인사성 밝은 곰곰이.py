import sys
input = lambda:sys.stdin.readline().strip()

ans = 0
chat = set()
for _ in range(int(input())):
    msg = input()
    
    if msg == "ENTER":
        chat = set()
        continue
    
    if msg not in chat:
        chat.add(msg)
        ans += 1

print(ans)