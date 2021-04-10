# 1260번 DFS와 BFS

[문제 보러가기](https://www.acmicpc.net/problem/1260)

🚩 `그래프 이론`, `그래프 탐색`, `DFS`, `BFS`

<br>

## 🅰 설계

처음에 인접리스트로 풀었는데 인풋값을 뭘 먼저 받느냐에 따라 dfs에서 순서가 달라져서 인접행렬로 풀었다. 

(같은 거리의 노드라면 숫자가 작은 순으로 진행되야 하기 때문)

dfs는 재귀여서 그냥 바로바로 출력하고자 함수 내에 print처리했고, bfs는 queue를 이용해서 풀었다.

<br>

## 🅱 최종 코드



```python
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
```

<br>

## ✅ 후기

그동안 그냥 풀었는데 순서를 지키면서 출력하려니 DFS가 어려웠다.