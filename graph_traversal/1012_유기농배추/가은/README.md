# 1012번 유기농 배추
[문제 보러가기](https://www.acmicpc.net/problem/1012)

## 🅰 설계

 :one: DFS 안 쓰고 풀기

1. 전체를 탐색하면서 1의 개수를 세서 벌레 += 1

2. 왼쪽이나 위에 1이 있으면 이전에 센 것(연결된 것)으로 생각하고 벌레 -= 1

   ```python
   T = int(input())
   
   for tc in range(1, T+1):
       # 가로길이 M, 세로길이 N, 배추개수 K
       M, N, K = map(int, input().split())
       # 배추밭 만들기
       cab = [[0] * M for _ in range(N)]
       for _ in range(K):
           r, c = map(int, input().split())
           cab[c][r] = 1
       print(cab)
   
       # 델타 상좌
       dr = [-1, 0]
       dc = [0, -1]
   
       worm = 0
       for i in range(N):
           for j in range(M):
               if cab[i][j]:
                   worm += 1
                   for d in range(4):
                       row = i + dr[d]
                       col = j + dc[d]
                       if row == -1 or col == -1:
                           continue
                       if cab[row][col]:
                           worm -= 1
                           break
       print(worm)
   ```

3. 틀린 이유

   ```
   [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],]
   오른쪽이랑 이어졌을 때 (2, 3)에서 오류남
   ```



:two: 최종 DFS

1. 전체를 탐색해서 배추가 있으면 벌레 += 1

2. dfs 함수로 벌레 += 1한 배추에 인접한 배추들을 다 없애준다

   벌레가 중복되지 않는다! :happy:

```python
def dfs(i, j):
    global worm
    if cab[i][j]:
        cab[i][j] = 0
        for d in range(4):
            row = i + dr[d]
            col = j + dc[d]
            if row == -1 or row == N or col == -1 or col == M:
                continue
            dfs(row, col)
    else:
        return


for tc in range(1, T+1):
    # 가로길이 M, 세로길이 N, 배추개수 K
    M, N, K = map(int, input().split())
    # 배추밭 만들기
    cab = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        cab[c][r] = 1
    # print(cab)

    # 델타 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 전체를 탐색한다.
    worm = 0
    for i in range(N):
        for j in range(M):
            # 배추가 있으면
            if cab[i][j]:
                # 벌레를 놓고
                worm += 1
                # 나머지 인접한 곳은 배추표시를 없앤다.(벌레 중복 피하기)
                dfs(i, j)

    print(worm)

```




## ✅ 후기
문제가 의도한 알고리즘을 사용해서 푸는 게 오류를 줄이고 좋은 것같다. :expressionless:

DFS가 잘 생각이 안나서 다른 방법으로 풀었다가 반례를 찾는데에 시간을 버리고 결국은 DFS로 풀어야 했다.



DFS문제만 보면 자신이 너무 없어서 다르게 풀 방법만 생각했는데 차근 차근 주석을 달면서 사고의 흐름을 가져가면서 풀어보자!!