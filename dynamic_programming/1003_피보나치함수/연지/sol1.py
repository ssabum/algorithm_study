import sys
sys.stdin = open("input.txt")

def f(n):
    cnt_0 = [1,0]  # 0 호출횟수 기록하는 리스트
    cnt_1 = [0,1]  # 1 호출횟수 기록하는 리스트

    for i in range(2, n+1):
        cnt_0.append(cnt_0[i-1] + cnt_0[i-2])  # 이전 두 단계의 0 호출횟수를 더함
        cnt_1.append(cnt_1[i-1] + cnt_1[i-2])
    return cnt_0, cnt_1


T = int(input())
for tc in range(T):
    N = int(input())
    print("{} {}".format(f(N)[0][N], f(N)[1][N]))
