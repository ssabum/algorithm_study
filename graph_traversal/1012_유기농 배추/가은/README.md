# 1012번 유기농 배추
[문제 보러가기](https://www.acmicpc.net/problem/1012)

## 🅰 설계

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

결국은 BFS로 풀어야 할 거같은데 기억이 안 난다..




## ✅ 후기
문제가 의도한 알고리즘을 사용해서 푸는 게 오류를 줄이고 좋은 것같다. :expressionless:

BFS가 잘 생각이 안나서 다른 방법으로 풀었다가 반례를 찾는데에 시간을 버리고 결국은 BFS로 풀어야 했다.