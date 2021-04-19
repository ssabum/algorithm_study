# 1697번 숨바꼭질
[문제 보러가기](https://www.acmicpc.net/problem/1697)

## 🅰 설계

* 수빈이와 동생의 위치가 주어졌을때 수빈이가 동생의 위치로 이동할 수 있는 최소 거리를 찾는 것이 문제의 목표이다.

* 현재의 위치에서 이동할 수 있는 수단이 `3가지`이기 때문에 `BFS`로 접근하면 되겠다 생각하고 풀이해 나갔지만 문제에서 요구하는 정확한 알고리즘 구조를 짜기가 어려웠다...💦

* 또한 처음에 또 실수한 부분이 아무생각 없이 `list`를 이용해 `queue`를 구현하려 했다는 것이다.

  `python`에서 `list`로 `queue`를 구현하면 시간복잡도가 `O(n)`으로 매우 느리다. 따라서 `collections`의 `deque`를 이용해야 하며, 이때 시간복잡도는 `O(1)`로 빠르다.

### ✔  정답 코드 구글링

```python
from collections import deque

def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            print(time[v])
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[v] + 1
                q.append(next_step)

MAX = 100001
N, K = map(int, input().split())
time = [0]*MAX
bfs()

```

---


## ✅ 후기
* 아직까지도 `BFS`, `DFS` 를 내 입맛대로 자유롭게 구현하는 것이 어려웠고..

  `D1`이라는 난이도에 쫄았던 것 같다;; 많은 배움이 필요하다...하기 싫네...