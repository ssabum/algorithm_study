import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)
import copy

# 하얀 색종이 개수, 파란 색종이 개수 구하기

N = int(input()) # 전체 종이의 한 변의 길이
paper = [list(map(int, input().split())) for _ in range(N)] # 종이
# print(paper)

def real_divide1(temp):
    p = []
    for x in temp[:N // 2]:
        p.append(x[:N // 2])
    return p

def real_divide2(temp):
    p = []
    for x in temp[:N // 2]:
        p.append(x[N // 2:])
    return p

def real_divide3(temp):
    p = []
    for x in temp[N // 2:]:
        p.append(x[:N // 2])
    return p

def real_divide4(temp):
    p = []
    for x in temp[N // 2:]:
        p.append(x[N // 2:])
    return p

# 각 종이 조각의 색이 하나일 때까지
white = 0
blue = 0

def divide(board):
    global white, blue
    N = len(board)
    if N == 1:
        return
    flag = True
    for i in range(N):
        for j in range(N):
            # 다른 게 하나라도 있으면을 어떻게 처리할지 모르겠다.
            if board[i][j] != board[0][0]:
                flag = False
                break
        if not flag:
            break
    if not flag:
        divide(real_divide1(board)), divide(real_divide2(board)), divide(real_divide3(board)), divide(real_divide4(board))

        
        # p = []
        # for x in temp[:N//2]:
        #     p.append(x[:N//2])
        # divide(p)
        # # paper가 4 * 4로 변경됐는데 원래 paper 8 * 8 를 가져오려면 어떻게 하지?
        # p = []
        # for x in temp[:N//2]:
        #     p.append(x[N//2:])
        # divide(p)
        
        # p = []
        # for x in temp[N//2:]:
        #     p.append(x[:N//2])
        # divide(p)
        
        # p = []
        # for x in temp[N//2:]:
        #     p.append(x[N//2:])
        # divide(p)

    else:
        if paper[0][0] == 1:
            blue += 1
        else:
            white += 1
        return

print(divide(paper))
print(blue, white)