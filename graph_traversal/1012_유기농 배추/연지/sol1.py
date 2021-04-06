import sys
sys.setrecursionlimit(10000)

def dfs(r,c):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    a[r][c] = -1  # 방문체크
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:  # 범위체크
            continue
        if a[nr][nc] == 1:
            a[nr][nc] = -1  # 방문체크
            dfs(nr,nc)

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())  # M:가로길이(열 길이), N:세로길이(행 길이), K:배추개수
    a = [[0] * M for _ in range(N)]  # 배추밭

    for _ in range(K):  # 배추 1로 바꾸기
        c, r = map(int, input().split())
        a[r][c] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == 1:  # 배추면 카운트+1 & 방향 탐색
                dfs(i,j)
                cnt += 1

    print(cnt)