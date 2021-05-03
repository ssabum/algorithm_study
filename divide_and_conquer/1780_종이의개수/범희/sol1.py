import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

result = {"-1": 0, "0": 0, "1": 0}

# 체크 함수
def check(row, col, N):
    value = data[row][col]
    for i in range(N):
        for j in range(N):
            if value != data[row + i][col + j]:
                # 9분할
                check(row, col, N // 3)
                check(row, col + N // 3, N // 3)
                check(row, col + N * 2 // 3, N // 3)
                check(row + N // 3, col, N // 3)
                check(row + N // 3, col + N // 3, N // 3)
                check(row + N // 3, col + N * 2 // 3, N // 3)
                check(row + N * 2 // 3, col, N // 3)
                check(row + N * 2 // 3, col + N // 3, N // 3)
                check(row + N * 2 // 3, col + N * 2 // 3, N // 3)
                return
    result[str(value)] += 1

check(0, 0, N)
# 결과 출력
print(result["-1"])
print(result["0"])
print(result["1"])