import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    ans = int(n ** .5)
    
    return ans + (ans ** 2 < n)
    
if __name__ == "__main__":
    print(main())
