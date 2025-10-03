import sys
input = lambda: sys.stdin.readline().strip()
from itertools import accumulate
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from bisect import bisect_left

INF = float('inf')

def main():
    ans = []

    trie = dict()

    n = int(input())
    for _ in range(n):
        _, *a = input().split()
        
        nxt = trie
        for w in a:
            if w not in nxt:
                nxt[w] = dict()
            nxt = nxt[w]

    def dfs(trie, depth):
        if not trie: return

        for w in sorted(trie):
            ans.append('--' * depth + w)
            dfs(trie[w], depth + 1)

    dfs(trie, 0)

    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
