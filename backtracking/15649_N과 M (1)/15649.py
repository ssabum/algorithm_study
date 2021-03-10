# 백트래킹 -> 재귀함수 사용
def DFS():
    if len(s) == M:
        print(*s)
        return

    for i in range(1, N+1):  # 1~N까지 숫자 순회하면서
        if visited[i]:  # 이미 방문했으면 패쓰
            continue

        # 방문 안했으면 방문체크 후, 출력 리스트에 넣음
        visited[i] = True
        s.append(i)
        DFS()  # 함수 다시 호출
        s.pop()  # 원상복귀 과정 필요
        visited[i] = False


        
N, M = map(int, input().split())  # N:주어진 수, M:수열의 길이
s = []  # 출력 수열 넣을 리스트 (stack)
visited = [False] * (N+1)  # 방문체크 할 리스트
DFS()  # 인자가 딱히 없어서 안넣음..