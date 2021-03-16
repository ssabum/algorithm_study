# 2164번 카드2
[문제 보러가기]()

## 🅰 설계

1. 일반적인 큐

   ```python
   cards = []
   for i in range(1, N+1):
       cards.append(i)
   
   # 한 장 남을 때까지
   while len(cards) > 1:
       # 1. 제일 위 버린다
       cards.pop(0)
       # 2. 제일 위 아래로
       cards.append(cards.pop(0))
   ```

   시간초과 :face_with_head_bandage:

2. 짝수 인덱스를 지우는 방식

   ```python
   while len(cards) > 1:
       for i in range(0, (len(cards)+1)//2):
           cards.pop(i)
           # print(cards)
   ```

   시간초과 :face_with_head_bandage:

3. 결과값에서 규칙찾기

   N의 값이 2의 거듭제곱값이 될때마다

   2 4 8 16 ... 반복된다.

   ```
   1
   2
   2
   4
   2
   4
   6
   8
   2
   4
   6
   8
   10
   12
   14
   16
   2
   4
   6
   8
   10
   12
   14
   16
   18
   20
   22
   24
   26
   ```

   결과의 규칙성으로 찾는 게 맞는 방법인 것같지만

   능력부족

## ✅ 후기

시간초과가 세상에서 제일 짜증난다는 점

거듭제곱마다 값이 반복된다는 것을 코드로 짜지 못하는 내 자신이 싫어졌다