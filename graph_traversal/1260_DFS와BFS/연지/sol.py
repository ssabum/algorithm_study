import sys
sys.stdin = open("input.txt")

def DFS(V):
    visited[V] = 1  # 방문체크
    print(V, end=' ')  # 재귀여서 바로 출력
    for v in range(1, N+1):
        if not visited[v] and edge_matrix[V][v] == 1:
            DFS(v)


def BFS(V):
    queue = [V]  # 출발점
    visited = [V]  # 방문
    while queue:
        t = queue.pop(0)
        for v in range(1, N+1):
            if v not in visited and edge_matrix[t][v] == 1:
                queue.append(v)
                visited.append(v)
    return visited


T = int(input())
for tc in range(1, T+1):
    N, M, V = map(int, input().split())  # N:정점개수, M:간선개수, V:시작정점 번호
    edge_matrix = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        edge_matrix[s][e] = 1
        edge_matrix[e][s] = 1

    visited = [0] * (N+1)  # dfs 방문체크용

    DFS(V)
    print()
    print(*BFS(V))