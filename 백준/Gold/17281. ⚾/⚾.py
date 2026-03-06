import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
from itertools import permutations as perm
from heapq import heappop, heappush

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n = int(input())
    graph = [tuple(map(int, input().split())) for _ in range(n)]

    def game(user):
        score = 0
        attack = 0
        for i in range(n):
            b1 = b2 = b3 = 0
            out = 0
            while out < 3:
                cur = graph[i][user[attack]]
                if cur == 0:
                    out += 1
                elif cur == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif cur == 2:
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif cur == 3:
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                elif cur == 4:
                    score += b1 + b2 + b3 + 1
                    b1 = b2 = b3 = 0

                
                attack = (attack + 1) % 9
        
        return score

    ans = 0
    for case in perm(range(1, 9), 8):
        ans = max(ans, game(case[:3] + (0,) + case[3:]))

    return ans

if __name__ == "__main__":
    print(main())
