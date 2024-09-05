import sys
input = lambda:sys.stdin.readline().strip()

def main():
    n = int(input())

    graph = [[] for _ in range(n+1)]

    for _ in range(n):
        a, *b = list(map(int, input().split()))

        for i in range(0, len(b)-1, 2):
            graph[a].append((b[i], b[i+1]))
    
    def dfs(start):
        visited = set()
        cost = 0
        end = start

        stack = [(start, 0)]
        while stack:
            u, ucost = stack.pop()
            if u not in visited:
                visited.add(u)
                if ucost > cost:
                    cost = ucost
                    end = u
                for v, vcost in graph[u]:
                    if v not in visited:
                        stack.append((v, ucost + vcost))
        
        return end, cost
    
    start, _ = dfs(1)
    return dfs(start)[1]

if __name__ == "__main__": 
    print(main())
