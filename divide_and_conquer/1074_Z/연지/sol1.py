import sys
sys.stdin = open("input.txt")

def divide(s_x, s_y, N):
    global cnt
    if N == 2:
        if s_x == r and s_y == c:  # 1위치
            print(cnt)
            return
        if s_x == r and s_y+1 == c:  # 2위치
            cnt += 1
            print(cnt)
            return
        if s_x+1 == r and s_y == c:  # 3위치
            cnt += 2
            print(cnt)
            return
        if s_x+1 == r and s_y+1 == c:  # 4위치
            cnt += 3
            print(cnt)
            return
        else:
            cnt += 4
            return
    else:
        half = N // 2
        if s_x <= r < s_x + half and s_y <= c < s_y + half:  # 1사분면
            divide(s_x, s_y, half)
        elif s_x <= r < s_x + half and s_y + half <= c < s_y + 2*half:  # 2사분면
            cnt += half*half
            divide(s_x, s_y + half, half)
        elif s_x + half <= r < s_x + 2*half and s_y <= c < s_y + half:  # 3사분면
            cnt += half*half*2
            divide(s_x + half, s_y, half)
        elif s_x + half <= r < s_x + 2*half and s_y + half <= c < s_y + 2*half:  # 4사분면
            cnt += half*half*3
            divide(s_x + half, s_y + half, half)


N, r, c = map(int, input().split())

cnt = 0
divide(0,0,2**N)