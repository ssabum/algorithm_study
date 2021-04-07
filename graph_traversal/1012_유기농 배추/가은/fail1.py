import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 가로길이 M, 세로길이 N, 배추개수 K
    M, N, K = map(int, input().split())
    # 배추밭 만들기
    cab = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        cab[c][r] = 1
    print(cab)

    # 델타 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    worm = 0
    for i in range(N):
        for j in range(M):
            if cab[i][j]:
                worm += 1
                for d in range(4):
                    row = i + dr[d]
                    col = j + dc[d]
                    if row == -1 or col == -1:
                        continue
                    if cab[row][col]:
                        worm -= 1
                        break
    print(worm)
    # [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #  [0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    #  [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    #  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    # 오른쪽이랑 이어졌을 때 오류남
