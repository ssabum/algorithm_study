from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global visited
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and a[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))



N, M = map(int, input().split())
a = [list(map(int, input())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]  # 값 갱신할 2차원배열
bfs()

print("{}".format(visited[N-1][M-1]))

