from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

board = [input() for _ in range(n)]

ans = []

for i in range(n-7):
    for j in range(m-7):
        idx1 = 0
        idx2 = 0
        
        for k in range(i, i+8):
            for l in range(j, j+8):
                if ( k+l )%2 == 0:
                    if board[k][l] != "W":
                        idx1 += 1
                    if board[k][l] != "B":
                        idx2 += 1
                else:
                    if board[k][l] != "B":
                        idx1 += 1
                    if board[k][l] != "W":
                        idx2 += 1
        ans.append(min(idx1, idx2))

print(min(ans))