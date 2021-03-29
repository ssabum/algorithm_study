# 1012번_유기농 배추
[문제 보러가기](https://www.acmicpc.net/problem/1012)

## 🅰 설계

```python
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # m: 가로길이, n: 세로길이, k: 배추개수
    m, n, k = map(int, input().split())
    # 입력된 데이터에 맞춰 밭 만들어 주기
    field = list(list(0 for i in range(m)) for _ in range(n))
    # 밭에 배추 심기
    for i in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    # 지렁이 검사
    cnt = 0
    
# 이후 접근을 어떻게 해야할지...
```

## 🅰 모범답안

```python
t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and s[q][w] == 1:
                s[q][w] = 0
                queue.append([q, w])
for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
    for q in range(n):
        for w in range(m):
            if s[q][w] == 1:
                bfs(q, w)
                s[q][w] = 0
                cnt += 1
    print(cnt)
```

---


## ✅ 후기
* 데이터를 받아오고 기본 `base`에 넣어주는 부분까지는 구현했지만 `bfs`를 돌면서 탐색하는 것이 아직 익숙치 않아 한참을 노트와 키보드만 끄적거리고 두들기다가 문제를 해결하지 못했다.

* 이후 검색을 통해 풀이방법을 알 수 있었고 보다 많음 `bfs`, `dfs` 문제를 풀어보면서 숙달해야겠다고 느꼈다.😨

