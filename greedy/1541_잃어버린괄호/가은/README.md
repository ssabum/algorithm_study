# 1541번 잃어버린 괄호
[문제 보러가기](https://www.acmicpc.net/problem/1541)

## 🅰 설계

1. 문제 풀이 계획

   1. 첫 `-` 위치를 찾는다.

   2. 그것을 기준으로 input을 나눈다.

   3. `-` 앞은 다 더해주는 부분

   4. `-` 뒤는 다 빼주는 부분

2. fail1.py

   input을 str자체로 받아서 eval과 replace함수를 사용했다.

   ```python
   input_str = input()
   # 첫 - 를 찾는다
   first_minus = input_str.find('-') 
   # - 가 없는 경우
   if first_minus == -1: # find: 해당 문자열이 없으면 -1 return
       print(eval(input_str))
   else:
       # 첫 - 를 기준으로 나눈다.
       plus_part = input_str[:first_minus]
       minus_part = input_str[first_minus:]
       # minus_part의 + 를 - 로 바꾸기
       cal = plus_part + minus_part.replace('+', '-')
       # 문자열 식 계산하기
       print(eval(cal))
   ```

   :exclamation: syntax error : eval 함수는 '012'는 계산하지 못한다.

3. sol1.py

   input을 연산자기준으로 나눠서 숫자만 리스트에 담아서 계산한다.

   ```python
   import re
   input_str = input()
   # 첫 - 를 찾는다
   first_minus = input_str.find('-') 
   # - 가 없는 경우
   if first_minus == -1: # find: 해당 문자열이 없으면 -1 return
       print(eval(input_str))
   else:
       # 첫 - 를 기준으로 나눈다.
       # + 할 부분
       plus_part = input_str[:first_minus]
       plus_list = plus_part.split('+')
       # print(plus_list)
       # - 할 부분
       minus_part = input_str[first_minus+1:]
       minus_list = re.split('[-, +]', minus_part)
       # print(minus_list)
       # 계산하기
       total = 0
       for x in plus_list:
           total += int(x)
       for x in minus_list:
           total -= int(x)
       print(total)
   ```


## ✅ 후기
1. 여러개로 split하는 방법

   numbers = re.split('[-, +]', input_str)

2. 문자열로 된 식 계산하기

   eval('5+4')

   :exclamation: eval()에는 '012'같은 숫자들이 들어갈 수 없다.



모르는 문제는 빨리 검색해서 보는 게 정말 맞는 방법이라는 생각이 들었다. 함수자체가 저렇게 생겨먹은 걸 혼자 고민해서 어떻게 알겠어