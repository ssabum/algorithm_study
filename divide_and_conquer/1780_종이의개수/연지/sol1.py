# 확인하는 함수
def checking(s_x, s_y, length):  # 시작 x, y좌표, 종이 길이
    global res
    check = []
    for i in range(s_x, s_x+length):
        for j in range(s_y, s_y+length):
            if a[i][j] not in check:
                check.append(a[i][j])
            if len(check) >= 2:
                # 함수 나누고 끝내기
                divide(s_x, s_y, length)
                return
    # 같은 종이로 이루어진 경우
    if check[0] == -1:
        res[0] += 1
    elif check[0] == 0:
        res[1] += 1
    elif check[0] == 1:
        res[2] += 1


# 3으로 나누는 함수
def divide(s_x, s_y, length):
    global res
    if length == 1:
        res[a[s_x][s_y]] += 1
        return  # 더이상 나누지 않음
    k = length//3
    checking(s_x, s_y, k)
    checking(s_x, s_y+k, k)
    checking(s_x, s_y+2*k, k)
    checking(s_x+k, s_y, k)
    checking(s_x+k, s_y+k, k)
    checking(s_x+k, s_y+2*k, k)
    checking(s_x+2*k, s_y, k)
    checking(s_x+2*k, s_y+k, k)
    checking(s_x+2*k, s_y+2*k, k)



N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
res = [0, 0, 0]  # -1개수, 0개수, 1개수
checking(0, 0, N)

print(res[0])
print(res[1])
print(res[2])
