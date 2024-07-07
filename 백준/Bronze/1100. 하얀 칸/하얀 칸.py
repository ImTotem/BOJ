import sys
input = lambda:sys.stdin.readline().strip()

def main():
    board = [list(input()) for _ in range(8)]
    
    return sum(
        (not (r+c)%2) and board[r][c] == 'F'
        for r in range(8)
        for c in range(8)
    )

print(main())