import sys
sys.stdin = open("input.txt")

from collections import deque
N, M = map(int, input().split()) # N : 유저의 수, M : 친구 관계의 수
edge_list = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    edge_list[n1].append(n2)
    edge_list[n2].append(n1)
print(edge_list)


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

print(arr)
min_value = N**2
min_index = 0
for j in range(N):
    if arr[j] < min_value:
        min_value = arr[j]
        min_index = j

print(min_index+1)


def max_edge(arr):
    max = 0
    max_e = 0
    for i in range(len(arr)):
        if len(arr[i]) > max:
            max_e = i
    return max_e

# print(max_edge(edge_list))
