# 2630번 색종이 만들기

[문제 보러가기]()

## 🅰 설계

1. 진짜로 색종이를 자르는 것처럼 리스트 슬라이싱으로 자르면서 풀기

   * 잘린 색종이 부분의 색이 다 같은지 확인하는 방법

     첫번째 원소의 색과 다른 색이 하나라도 있는지 체크! 

     ```python
     import sys
     sys.stdin = open("input.txt")
     sys.setrecursionlimit(10**6)
     import copy
     
     # 하얀 색종이 개수, 파란 색종이 개수 구하기
     
     N = int(input()) # 전체 종이의 한 변의 길이
     paper = [list(map(int, input().split())) for _ in range(N)] 
     
     # 각 종이 조각의 색이 하나일 때까지
     white = 0
     blue = 0
     
     def divide(board):
         global white, blue
         N = len(board)
         if N == 1:
             return
         flag = True
         for i in range(N):
             for j in range(N):
                 # 다른 게 하나라도 있으면을 어떻게 처리할지 모르겠다.
                 if board[i][j] != board[0][0]:
                     flag = False
                     break
             if not flag:
                 break
         if not flag:
             # 이 부분 한 줄로 처리 가능
             p = []
             for x in temp[:N//2]:
                 p.append(x[:N//2])
             divide(p)
             # paper가 4 * 4로 변경됐는데 원래 paper 8 * 8 를 가져오려면 어떻게 하지?
             p = []
             for x in temp[:N//2]:
                 p.append(x[N//2:])
             divide(p)
             
             p = []
             for x in temp[N//2:]:
                 p.append(x[:N//2])
             divide(p)
             
             p = []
             for x in temp[N//2:]:
                 p.append(x[N//2:])
             divide(p)
     
         else:
             if paper[0][0] == 1:
                 blue += 1
             else:
                 white += 1
             return
     
     print(blue, white)
     ```

     

   * paper가 4 * 4로 변경됐는데 원래 paper 8 * 8 를 가져오려면 어떻게 하지?

     * deepcopy로 해결하려다가 실패 :sweat:

     * 함수를 만들어서 종이를 자르는 방법 => 한 줄으로 작성가능

       :sweat: 매번 새로운 종이를 잘라서 시간이 너무 오래걸림 ㅠㅜㅜㅠ

       ```python
       ##########################################
       def real_divide1(temp):
           p = []
           for x in temp[:N // 2]:
               p.append(x[:N // 2])
           return p
       
       def real_divide2(temp):
           p = []
           for x in temp[:N // 2]:
               p.append(x[N // 2:])
           return p
       
       def real_divide3(temp):
           p = []
           for x in temp[N // 2:]:
               p.append(x[:N // 2])
           return p
       
       def real_divide4(temp):
           p = []
           for x in temp[N // 2:]:
               p.append(x[N // 2:])
           return p
       ###########################################
       N = int(input()) 
       paper = [list(map(int, input().split())) for _ in range(N)] 
       
       white = 0
       blue = 0
       
       def divide(board):
           global white, blue
           N = len(board)
           if N == 1:
               return
           flag = True
           for i in range(N):
               for j in range(N):
                   if board[i][j] != board[0][0]:
                       flag = False
                       break
               if not flag:
                   break
           if not flag:
               ############################################
               divide(real_divide1(board)), divide(real_divide2(board)), divide(real_divide3(board)), divide(real_divide4(board))
               ############################################
           else:
               if paper[0][0] == 1:
                   blue += 1
               else:
                   white += 1
               return
           
       print(blue, white)
       ```

2. 종이 자르지 않고 원래 색종이에서 탐색

   * 잘린 종이색이 같은지 확인하는 방법

     합으로 판별해보자

   ```python
   import sys
   sys.stdin = open("input.txt")
   
   # 하얀 색종이 개수, 파란 색종이 개수 구하기
   
   N = int(input()) # 전체 종이의 한 변의 길이
   paper = [list(map(int, input().split())) for _ in range(N)] # 종이
   
   # print(paper)
   
   white = 0
   blue = 0
   
   
   # 시작점이랑 탐색할 영역을 지정해주면서 탐색하는 거야
   def divide(board, row, col, n):
       global white, blue
       
       if n == 1: # 세어주고 return 해야 돼
           if board[row][col] == 1:
               blue += 1
           else:
               white += 1
           return
       
       # 확인하자 같은 색인지
       check = 0
       for i in range(n):
           for j in range(n):
               check += board[row+i][col+j]
   
       # 같은 색이면
       if check == 0:
           white += 1
       elif check == n**2:
           blue += 1
   	
       # 왜 이렇게 했을 때 안 되는지?
       # if n == 1:
       #     return
   
       # 아니면 나눠서 탐색
       else:
           divide(board, row, col, n//2)
           divide(board, row, col+n//2, n//2)
           divide(board, row+n//2, col, n//2)
           divide(board, row+n//2, col+n//2, n//2)
   
   divide(paper, 0, 0, N)
   print(white, blue)
   
   ```

   :a: 알아버렸다!!!
   
   ```python
   # 왜 이렇게 했을 때 안 되는지?
       # if n == 1:
       #     return
   ```
   
   if가 갑자기 옮겨지면서 if, else가 엉겨서 else가 n!=1일때로 바껴버렸다!!



## ✅ 후기

1. 2차원 리스트는 `global`없이도 global변수라는 점
2. 한 줄에 작성하면 같은 board값이 들어간다.
3. 원래 2차원 리스트를 변경하지 않으려면 시작점 범위를 조절해서 탐색하는 방법!