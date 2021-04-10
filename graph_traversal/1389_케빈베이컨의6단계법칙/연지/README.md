# 1389번 케빈 베이컨의 6단계 법칙

[문제 보러가기](https://www.acmicpc.net/problem/1389)

🚩 `그래프 이론`, `그래프 탐색`, `BFS`, `플로이드-와샬`

<br>

## 🅰 설계

그림을 그려보니 BFS여서 BFS로 풀었다. M (1 ≤ M ≤ 5,000)의 범위가 너무 커서 deque 모듈로 풀었다.

1. 틀림 (fail)

~~진짜 맞왜틀(맞는데 왜 틀린거지) ?!~~  👈  나는 바보였다.. 번호가 가장 작은 사람을 출력하는 문제였는데 가장 작은 경우의 수를 출력했다;;

```python
from collections import deque

def BFS(i):
    visited = [0] * (N+1)
    queue.append(i)
    visited[i] = 1
    while queue:
        t = queue.popleft()
        for v in edge_list[t]:
            if not visited[v]:
                visited[v] = visited[t]+1
                queue.append(v)
    return sum(visited)


N, M = map(int, input().split())  # N:유저의 수, M: 친구관계 수
edge_list = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    edge_list[s].append(e)
    edge_list[e].append(s)

queue = deque()

min = 5000
for i in range(1, N+1):
    if BFS(i) < min:
        min = BFS(i)

print(min-N)
```

<br>

## 🅱 최종 코드

가장 작은 경우의 수의 인덱스를 출력하니 맞았다

```python
from collections import deque

def BFS(i):
    visited = [0] * (N+1)
    queue.append(i)
    visited[i] = 1
    while queue:
        t = queue.popleft()
        for v in edge_list[t]:
            if not visited[v]:
                visited[v] = visited[t]+1
                queue.append(v)
    return sum(visited)


N, M = map(int, input().split())  # N:유저의 수, M: 친구관계 수
edge_list = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    edge_list[s].append(e)
    edge_list[e].append(s)

queue = deque()
res = []
for i in range(1, N+1):
    res.append(BFS(i))

print(res.index(min(res))+1)
```

<br>

## ✅ 후기

### 새롭게 알게 된 점

인덱스 찾는법 -> .index(`찾고싶은값`)

