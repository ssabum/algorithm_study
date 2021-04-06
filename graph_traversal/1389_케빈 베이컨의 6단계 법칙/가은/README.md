# 1389번 케빈 베이컨의 6단계 법칙
[문제 보러가기](https://www.acmicpc.net/problem/1389)

## 🅰 설계

1. bfs를 통해서 최소합을 구하려고 함.

   ```python
   from collections import deque
   N, M = map(int, input().split()) # N : 유저의 수, M : 친구 관계의 수
   edge_list = [[] for _ in range(N+1)]
   for _ in range(M):
       n1, n2 = map(int, input().split())
       edge_list[n1].append(n2)
       edge_list[n2].append(n1)
   print(edge_list)
   
   # 케빈 베이컨의 수
   min = N * N
   person = 0
   
   
   for i in range(1, N+1):
       # 시작 노드
       queue = deque([i])
       # 각 사람 별 케빈 베이커 수
       cnt = 0
       # 도착 노드 설정
       for j in range(1, N+1):
           # 시작노드 pass
           if i == j:
               continue
           # 방문
           visited = [0] * (1+N)
           while True:
               now = queue.popleft()
               # 도착노드 도착시 종료
               if now == j:
                   break
               if not visited[now]:
                   visited[now] = 1
                   for v in edge_list[now]:
                       queue.append(v)
   
       # 번호가 가장 작은 사람 출력
       if cnt < min:
           min = cnt
           person = i
   
   print(person)
   ```

   :arrow_right: 런타임에러로 실패

2. graph의 depth마다 count를 더하는 걸로 구해야 한다.

   전체를 탐색하는 것 == 각 노드에서 출발해서 모든 노드를  방문하는 것

    ```python
   from collections import deque
   N, M = map(int, input().split()) # N : 유저의 수, M : 친구 관계의 수
   edge_list = [[] for _ in range(N+1)]
   for _ in range(M):
       n1, n2 = map(int, input().split())
       edge_list[n1].append(n2)
       edge_list[n2].append(n1)
   
   # 케빈 베이컨의 리스트
   arr = []
   
   def bfs(i):
       # 시작 노드
       queue = deque([i])
       # 방문
       visited = [0] * (N+1)
       visited[i] = 1
       while queue:
           now = queue.popleft()
           for v in edge_list[now]:
               if not visited[v]:
                   queue.append(v)
                   visited[v] = visited[now] + 1
       arr.append(sum(visited))
       return
   
   for i in range(1, N+1):
       bfs(i)
   
   min_value = N**2
   min_index = 0
   for j in range(N):
       if arr[j] < min_value:
           min_value = arr[j]
           min_index = j
   
   print(min_index+1)
    ```

   

3. edge의 개수가 많은 것들끼리만 비교하면 더 효율적이지 않을까?

   아직 안해봄 그냥 아이디어!

   


## ✅ 후기
전체를 탐색하는 것 == 각 노드에서 출발해서 모든 노드를  방문하는 것

그냥 일반적인 bfs하면 된다!

dfs, bfs, 재귀가 발전이 없어서 슬픔.