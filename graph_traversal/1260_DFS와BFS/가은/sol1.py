from collections import deque
import sys
sys.stdin = open("input.txt")

T = 3

for tc in range(1, T+1):
    N, M, V = map(int, input().split())
    edge_input = [list(map(int, input().split())) for _ in range(M)]
    # print(edge_input)

    edge_list = [[] for _ in range(N+1)]
    for e in edge_input:
        n1, n2 = e
        edge_list[n1].append(n2)
        edge_list[n2].append(n1)
    # print(edge_list)

    # 갈 수 있는 노드
    stack = [V]
    # 방문 노드
    visited = [0] * (N+1)
    def dfs():
        while stack:
            # 현재
            now = stack.pop()
            # print(stack)
            # 방문 안 했을 때
            if not visited[now]:
                visited[now] = 1
                print(now, end=' ')
                # now에 연결된 node 찾기
                for v in reversed(sorted(edge_list[now])):
                    stack.append(v)
        print()

    dfs()

    queue = deque([V])
    visited = [0] * (N+1)

    def bfs():
        while queue:
            now = queue.popleft()
            if not visited[now]:
                visited[now] = 1
                print(now, end=' ')
                for v in sorted(edge_list[now]):
                    queue.append(v)
        print()

    bfs()

