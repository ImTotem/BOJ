import sys
input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush

INF = float('inf')

def main():
    n, m, k = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    pq = [(0, 1, 0)]
    dp = [[INF] * (k + 1) for _ in range(n + 1)]  # dp[visited[k]
    dp[1][0] = 0

    while pq:
        cur_cost, cur_node, cur_k = heappop(pq)

        if dp[cur_node][cur_k] < cur_cost:
            continue

        for next_cost, next_node in graph[cur_node]:
            next_sum_cost = cur_cost + next_cost

            if dp[next_node][cur_k] > next_sum_cost:
                heappush(pq, (next_sum_cost, next_node, cur_k))
                dp[next_node][cur_k] = next_sum_cost
            
            if cur_k < k and dp[next_node][cur_k+1] > cur_cost:
                heappush(pq, (cur_cost, next_node, cur_k+1))
                dp[next_node][cur_k+1] = cur_cost
       
    return min(dp[n])


if __name__ == "__main__":
    print(main())
