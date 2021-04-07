import sys
sys.setrecursionlimit(100000)
sys.stdin = open("input.txt")

T = int(input())

'''
배추 심어놓은 땅 (1) 찾기
인접해 있는 땅은 지렁이 한 마리면 충분하다. 
'''

def dfs(i, j):
    global worm
    if cab[i][j]:
        cab[i][j] = 0
        for d in range(4):
            row = i + dr[d]
            col = j + dc[d]
            if row == -1 or row == N or col == -1 or col == M:
                continue
            dfs(row, col)
    else:
        return


for tc in range(1, T+1):
    # 가로길이 M, 세로길이 N, 배추개수 K
    M, N, K = map(int, input().split())
    # 배추밭 만들기
    cab = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        cab[c][r] = 1
    # print(cab)

    # 델타 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 전체를 탐색한다.
    worm = 0
    for i in range(N):
        for j in range(M):
            # 배추가 있으면
            if cab[i][j]:
                # 벌레를 놓고
                worm += 1
                # 나머지 인접한 곳은 배추표시를 없앤다.(벌레 중복 피하기)
                dfs(i, j)

    print(worm)
