# 메모리초과
from collections import deque

def bfs(x):
    global res
    q = deque()
    q.append(x)
    visited = {x:1,}

    while q:
        x = q.popleft()
        if x == K:
            res = visited[x]-1
            return
        tmp = []  # 연결노드 담을 임시 리스트
        tmp.extend([x - 1, x + 1, 2 * x])
        for v in tmp:
            if not visited.get(v, 0):  # 방문 안했으면 방문체크
                visited[v] = visited[x]+1
                q.append(v)
        tmp = []  # 초기화


N, K = map(int, input().split())  # N:수빈, K:동생
res = 0
bfs(N)
print(res)