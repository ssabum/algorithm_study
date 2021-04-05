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