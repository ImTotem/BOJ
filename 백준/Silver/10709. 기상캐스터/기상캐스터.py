import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')

def main():
    h, w = map(int, input().split())
    ans = []
    
    for _ in range(h):
        _ans = []
        line = input()
        
        cloud = -1
        for i in range(w):
            if line[i] == 'c':
                cloud = i
            _ans.append([f'{i - cloud}', '-1'][cloud == -1])
    
        ans.append(' '.join(_ans))
    
    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
