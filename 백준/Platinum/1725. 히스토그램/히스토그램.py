import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    h = [int(input()) for _ in range(n)]
    h.append(0)

    stack = []
    ans = 0

    for i, cur in enumerate(h):
        while stack and h[stack[-1]] > cur:
            ih = h[stack.pop()]
            
            w = i - stack[-1]-1 if stack else i

            ans = max(ans, w * ih)
            
        stack.append(i)
    
    return ans

if __name__ == "__main__":
    print(main())
