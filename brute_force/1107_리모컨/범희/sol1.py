# N: 목표로 하는 채널번호(0~500000), M: 고장난 버튼의 개수(0~10)
N = int(input())
M = int(input())
# button: 숫자 버튼 / 고장난 버튼이 있으면 빼준다
button = {i for i in range(10)}
if M != 0:
    button -= set(map(int, input().split()))

# 100번에서 N번으로 +, - 버튼만 쓴 경우
cnt = abs(100 - N)
# 50만 채널인데 최악의 경우를 고려할 때
# 작은수에서 +만 사용(50만)에 큰수에서 -만 사용(50만)을 더하면 100만 가지의 경우의 수가 발생
for i in range(1000000):
    flag = True
    for j in str(i):
        if int(j) not in button:
            flag = False
            break
    if flag:
        # button으로 접근 할 수 있는 수에다가 목표 채널의 차이(+, - 으로 이동)를 더한 값
        cnt = min(cnt, len(str(i)) + abs(N-i))

print(cnt)


