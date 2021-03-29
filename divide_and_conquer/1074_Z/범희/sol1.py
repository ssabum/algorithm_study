import sys

result = 0

def z(n, x, y):
    global result
    # 기본이 되는 탈출 조건 생성
    if x == r and y == c:
        print(int(result))
        exit(0)

    if n == 1:
        result += 1
        return

    # 처음에 시간초과 떠서 경우의 수도 합쳐 주었다.
    # 하지만 나중에 알고보니 할 필요 없었다...
    if not (x <= r < x + n and y <= c < y + n):
        result += n * n
        return
    # 재귀함수
    z(n / 2, x, y)
    z(n / 2, x, y + n / 2)
    z(n / 2, x + n / 2, y)
    z(n / 2, x + n / 2, y + n / 2)

# 시간초과 안나기 위해 sys.stdin.readline사용...sibal...
n, r, c = map(int, sys.stdin.readline().split(' '))
z(2 ** n, 0, 0)