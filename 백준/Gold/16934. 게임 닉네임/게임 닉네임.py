import sys
input = lambda: sys.stdin.readline().strip()

INF = float('inf')

def main():
    n = int(input())
    nicks = [input() for _ in range(n)]
    
    trie = dict()
    ans = []

    for nick in nicks:
        nxt = trie
        tag = ''
        for i, c in enumerate(nick):
            if c not in nxt:
                nxt[c] = dict()
                if not tag: tag = nick[:i+1]
            nxt = nxt[c]
        
        if '.' not in nxt: nxt['.'] = 0
        nxt['.'] += 1
        
        if not tag: tag = nick
        if nxt['.'] > 1: tag += str(nxt['.'])

        ans.append(tag)

    return '\n'.join(ans)

if __name__ == "__main__":
    print(main())
