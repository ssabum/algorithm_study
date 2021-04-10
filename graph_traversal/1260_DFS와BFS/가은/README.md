# 1260번 DFS와 BFS
[문제 보러가기](https://www.acmicpc.net/problem/1260)

## 🅰 설계

기본적인 DFS, BFS 알고리즘을 사용한다.

**방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문한다**

부분을 처리하기 위해서 DFS 함수를 만들 때 해당 노드에 연결된 노드를 `reverse` 하여 stack에 쌓았다.

* 인접리스트

  ```python
  edge_list = [[] for _ in range(N+1)]
  for e in edge_input:
      n1, n2 = e
      edge_list[n1].append(n2)
      edge_list[n2].append(n1)
  ```

1. DFS

   ```python
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
   ```

2. BFS

   ```python
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
   ```

   


## ✅ 후기
BFS를 풀 때 visited를 초기화해줘야 했는데 함수는 재정의하는 것 이외의 방법을 찾아봐야겠다.

BFS, DFS를 너무 오랜만에 풀어서 이전에 풀었던 문제풀이를 참고했다! 그래도 한 번 풀어보니까 용기가 새록새록 :smile_cat: