import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # m: 가로길이, n: 세로길이, k: 배추개수
    m, n, k = map(int, input().split())
    # 입력된 데이터에 맞춰 밭 만들어 주기
    field = list(list(0 for i in range(m)) for _ in range(n))
    # 밭에 배추 심기
    for i in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    # 지렁이 검사
    cnt = 0