# 1389번_케빈 베이컨의 6단계 법칙
[문제 보러가기](https://www.acmicpc.net/problem/1389)

## 🅰 코드

```python
from collections import deque

def bfs(num, n):
    # 기본 base setting
    bacon = [0] * (n + 1)
    visited = [num]
    queue = deque()
    queue.append(num)

    while queue:
        # queue에서 popleft사용
        k = queue.popleft()
        for i in relation[k]:
            if i not in visited:
                bacon[i] = bacon[k] + 1
                visited.append(i)
                queue.append(i)
    return sum(bacon)

# n: 유저수(2~100), m: 관계수(1~5000)
n, m = map(int, input().split())
# 관계 dict생성 후 입력
relation = {i: [] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

result = []
for num in range(1, n + 1):
    result.append(bfs(num, n))

# index로 최소 관계를 구하고 관계이기 때문에 1을 더해준다
print(result.index(min(result)) + 1)

```

---


## ✅ 후기
* `BFS`를 이용하여 풀어내는 문제였다. 알고리즘 문제를 풀때마다 느끼는 거지만, 알고리즘 이해 자체는 어렵지 않지만 그것을 이용하여 문제를 풀어내는 것은 굉장히 어려운 것 같다;;
* 여담이지만 `케빈 베이컨`처럼 야리꾸리한 문제를 만들어서 자기이름을 붙이는 작자들은 도대체 어떤 사람들인지 궁금하다...🥴
