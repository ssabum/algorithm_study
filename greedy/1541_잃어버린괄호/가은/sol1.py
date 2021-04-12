import sys
sys.stdin = open("input.txt")

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