import sys
sys.stdin = open("input.txt")

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic_n = {}  # {'25': 'Pikachu'}. 숫자접근으로 문자출력용
dic_s = {}  # {'Pikachu': 25}. 문자접근으로 숫자출력용
for i in range(N):
    value = input().strip()
    dic_n[str(i+1)] = value
    dic_s[value] = i+1

for j in range(M):
    quest = input().strip()
    if quest.isdigit():  # 숫자면 문자출력
        print(dic_n[quest])
    if quest.isalpha():  # 문자면 숫자출력
        print(dic_s[quest])

