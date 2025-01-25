import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    
    return [2, 0, 1, 0][n % 4]

if __name__ == "__main__":
    print(main())