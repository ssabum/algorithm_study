import re
import sys
sys.stdin = open("input.txt")

'''
괄호를 쳐서 식의 값을 최소로 만들어야 한다.
- 가 나오면 그 뒤부터 다 minus로 처리할 수 있다.

* 새롭게 알게 된 내용
여러개로 split하는 방법
numbers = re.split('[-, +]', input_str)
문자열로 된 식 계산하기
eval('5+4')
'''

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

'''
syntax error 
eval()에는 '012'같은 숫자들이 들어갈 수 없다.
'''