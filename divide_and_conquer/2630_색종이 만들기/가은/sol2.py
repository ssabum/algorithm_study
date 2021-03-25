import sys
sys.stdin = open("input.txt")

# 하얀 색종이 개수, 파란 색종이 개수 구하기

N = int(input()) # 전체 종이의 한 변의 길이
paper = [list(map(int, input().split())) for _ in range(N)] # 종이

# print(paper)

white = 0
blue = 0


# 시작점이랑 탐색할 영역을 지정해주면서 탐색하는 거야
def divide(board, row, col, n):
    global white, blue

    if n == 1: # 세어주고 return 해야 돼
        if board[row][col] == 1:
            blue += 1
        else:
            white += 1
        return

    # 확인하자 같은 색인지
    check = 0
    for i in range(n):
        for j in range(n):
            check += board[row+i][col+j]

    # 같은 색이면
    if check == 0:
        white += 1
    elif check == n**2:
        blue += 1

    # if n == 1:
    #     return

    # 아니면 나눠서 탐색
    else:
        divide(board, row, col, n//2)
        divide(board, row, col+n//2, n//2)
        divide(board, row+n//2, col, n//2)
        divide(board, row+n//2, col+n//2, n//2)

divide(paper, 0, 0, N)
print(white, blue)



