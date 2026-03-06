import sys
input = lambda: sys.stdin.readline().rstrip()

INF = float('inf')
D = [0, 1, 0, -1, 0]

def main():
    n = int(input())

    trie = dict()

    for _ in range(n):
        _, *t = input().split()
        
        nxt = trie
        for w in t:
            if w not in nxt:
                nxt[w] = dict()
            nxt = nxt[w]
    
    ans = []
    def dfs(trie, depth):
        if not trie: return

        for w in sorted(trie):
            ans.append('--' * depth + w)
            dfs(trie[w], depth + 1)
    
    dfs(trie, 0)

    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
