import sys
input = lambda:sys.stdin.readline().strip()

from collections import deque

def main():
    n, q = map(int, input().split())

    b, cur, f = deque(), 0, deque()

    for _ in range(q):
        cmd, *page = input().split()

        if cmd == 'B':
            if not b: continue
            f.appendleft(cur)
            cur = b.popleft()

        elif cmd == "F":
            if not f: continue
            b.appendleft(cur)
            cur = f.popleft()
        elif cmd == "A":
            f = deque()
            if cur: b.appendleft(cur)
            cur = page[0]
        else:
            newb = deque()
            while b:
                c = b.popleft()
                if not newb or newb[-1] != c:
                    newb.append(c)
            b = newb
    
    print(cur)
    print(' '.join(b) if b else -1)
    print(' '.join(f) if f else -1)

main()