N = int(input())
dp_list = [0,0,1,1] # 0 ,1, 2, 3 의 최소 수 미리 저장

for i in range(4, N + 1) :
    # 먼저 1을 뺏을 경우 나오는 경우의 수 저장
    dp_list.append(dp_list[i-1] + 1)

    #2로 나누어질 경우 기존 1을 뺏을 경우의 수와 비교하여 최솟값 저장
    if i % 2 == 0 :
        dp_list[i] = min(dp_list[i], dp_list[i//2] + 1)

    #3으로 나누어질 경우 기존 1을 뺏을 경우의 수와 비교하여 최솟값 저장
    #여기서 2 또는 3으로 나누어질 경우 모든 경우를 봐야하므로 elif가 아닌 if로 설정
    if i % 3 == 0 :
        dp_list[i] = min(dp_list[i], dp_list[i//3] + 1)

print(dp_list[-1])