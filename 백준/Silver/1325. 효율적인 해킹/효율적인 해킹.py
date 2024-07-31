import sys
input = lambda:sys.stdin.readline().strip()

from collections import defaultdict, deque

def main():
    n, m = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    def bfs(n, graph, target):
        q = deque([target])
        visited = [False] * (n+1)
        visited[target] = True
        cnt = 1

        while q:
            for i in graph[q.popleft()]:
                if not visited[i]:
                    cnt += 1
                    q.append(i)
                    visited[i] = True
        
        return cnt
    
    maxi, ans = 0, []
    for i in range(n):
        cnt = bfs(n, graph, i+1)

        if maxi == cnt:
            ans.append(i+1)
        elif maxi < cnt:
            maxi = cnt
            ans = [i+1]
    
    return ' '.join(map(str, ans))


if __name__ == "__main__":
    print(main())
