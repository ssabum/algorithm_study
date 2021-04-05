import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())

    if M != 0:
        remote = {str(x) for x in range(10)}
        remote -= set(input().split())  # 사용가능한 버튼 뽑아냄

    min_cnt = abs(100-N)
    for i in range(1000001):  # iterable 순회하기 위해 str형으로 체킹
        num = str(i)
        for j in range(len(num)):
            if num[j] not in remote:  # 버튼에 없으면 건너뜀
                break
            if j == len(num)-1:  # 마지막 자리수에서 체킹
                min_cnt = min(min_cnt, abs(N-i)+len(num))

    print(min_cnt)