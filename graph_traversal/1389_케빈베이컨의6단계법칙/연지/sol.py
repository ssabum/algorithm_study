import sys
sys.stdin = open("input.txt")
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