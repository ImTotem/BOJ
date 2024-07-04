import sys
input = lambda:sys.stdin.readline().strip()

def valid(cur, prev):
    d = (abs(ord(cur[0]) - ord(prev[0])), abs(int(cur[1]) - int(prev[1])))
    return d in {(2, 1), (1, 2)}

def main():
    prev = input()
    start = prev
    visited = {start}

    ans = "Valid"
    for _ in range(35):
        cur = input()
        if cur in visited or not valid(cur, prev):
            ans = "Invalid"
        
        visited.add(cur)
        prev = cur
    
    if not valid(start, prev):
        ans = "Invalid"

    return ans

print(main())