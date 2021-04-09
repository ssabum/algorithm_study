import sys
sys.stdin = open("input.txt")

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []  # 인덱스접근(숫자접근)으로 문자출력용
dic = {}  # {'Pikachu': 25}. 문자접근으로 숫자출력용
for i in range(N):
    value = input().strip()
    lst.append(value)
    dic[value] = i+1

for j in range(M):
    quest = input().strip()
    if quest.isdigit():  # 숫자면 문자출력
        print(lst[int(quest)-1])
    if quest.isalpha():  # 문자면 숫자출력
        print(dic[quest])