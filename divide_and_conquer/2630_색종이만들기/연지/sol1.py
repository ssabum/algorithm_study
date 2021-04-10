import sys
sys.stdin = open("input.txt")

def divide(s_x,s_y,N):
    global cnt_w, cnt_b
    if N == 1 and a[s_x][s_y] == 0:
        cnt_w += 1
        return
    if N == 1 and a[s_x][s_y] == 1:
        cnt_b += 1
        return

    flag_w = 0
    flag_b = 0
    for i in range(s_x, s_x+N):
        for j in range(s_y, s_y+N):
            if flag_w == 0 and a[i][j] == 0:
                flag_w = 1
            elif flag_b == 0 and a[i][j] == 1:
                flag_b = 1
    N //= 2
    if flag_w == 1 and flag_b == 0:  # 전부 하얀색인 경우 -> 하얀색 카운트하고 끝
        cnt_w += 1
    if flag_w == 0 and flag_b == 1:  # 전부 파랑색인 경우 -> 파랑색 카운트하고 끝
        cnt_b += 1
    if flag_w == 1 and flag_b == 1:  # 둘다 나오면 쪼개기
        divide(s_x, s_y, N)
        divide(s_x + N, s_y, N)
        divide(s_x, s_y + N, N)
        divide(s_x + N, s_y + N, N)



N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
cnt_w, cnt_b = 0, 0
divide(0, 0, N)
print(cnt_w, cnt_b)