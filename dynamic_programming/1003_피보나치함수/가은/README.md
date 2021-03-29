# 1003번 피보나치 함수
[문제 보러가기](https://www.acmicpc.net/problem/1003)

## 🅰 설계

1. 피보나치 재귀함수에 0과 1을 세는 과정 추가

   ```python
   # 0의 개수
   count0 = 0
   # 1의 개수
   count1 = 0
   
   
   def fibo(n):
       global count0, count1
       if n == 0:
           count0 += 1
           return 0
       elif n == 1:
           count1 += 1
           return 1
       return fibo(n - 1) + fibo(n - 2)
   ```

   :exclamation: 시간초과가 날 거라고 생각하면서 작성했는데 예상은 빗나가지 않지ㅠ

2. memoization 적용

   ```python
   c = [[0, 0]] * (N + 1)
   def fibo2(n):
       global c
       if n == 0:
           c[0] = [1, 0]
           return c[0]
       elif n == 1:
           c[1] = [0, 1]
           return c[1]
       elif c[n] != [0, 0]:
           return c[n]
       else:
           a1, a2 = fibo2(n - 1)
           a3, a4 = fibo2(n - 2)
           c[n] = [a1 + a3, a2 + a4]
           return c[n]	
   ```

   오랜만에 푸니까 이 부분 빼먹어서 틀렸었음

   ```python
   elif c[n] != [0, 0]:
           return c[n]
   ```

   

## ✅ 후기

memoization 기억 안나서 검색했는데도 내가 제대로 풀고 있는지도 몰랐다.

역시 알고리즘은 꾸준히 풀어야해.

또 백준은 정답 output과 데이터형식이 다르거나 하면 런타임에러가 나니까 당황하지 말자!