import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]

    def place(x, y, size):
        for i in range(y, y + size):
            for j in range(x, x + size):
                if not (0 <= j < m and 0 <= i < n): return False
                if board[i][j] == 'x': return False
        
        for i in range(y, y + size):
            for j in range(x, x + size):
                if not (0 <= j < m and 0 <= i < n): return False
                board[i][j] = 'x'

        return True

    def all_place(size):
        for y in range(n):
            for x in range(m):
                if place(x, y, size): return True
        
        return False

    user = ['pizza', 'sewon']
    ans = False

    while True:
        if all_place(3) or all_place(1):
            ans = not ans
        else:
            break

    return user[ans]

if __name__ == "__main__":
    for _ in range(int(input())):
        print(main())
