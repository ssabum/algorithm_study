# 1620번 나는야포켓몬마스터이다솜
[문제 보러가기](https://www.acmicpc.net/problem/1620)

## 🅰 설계

1. fail.py
   1. 숫자면 인덱스로 해당 포켓몬이름을 찾는다.
   2. 문자면 그 문자를 index함수로 찾으면 인덱스를 알 수 있다.

   

1. sol1.py

   1. 포켓몬 리스트와 딕셔너리를 만든다.
   2. 숫자면 똑같이 리스트에서 인덱스로 찾는다.
   3. 문자면 딕셔너리에서 찾으면 시간복잡도가 상수

   ```python
   N, M = map(int, input().split()) # N: 포켓몬 개수, M: 문제의 개수 1~100,000
   
   # 포켓몬
   pocket_list = []
   pocket_dict = {}
   for i in range(1, N+1):
       pocket = input()
       pocket_list.append(pocket)
       pocket_dict[pocket] = i
   # print(pocket)
   
   #문제
   problems = []
   for _ in range(M):
       pro = input()
       # 숫자문제이면
       if pro.isdigit():
           print(pocket_list[int(pro)-1])
       # 알파벳문제이면
       else:
           # print(pocket.index(pro)+1) # index 시간초과 O(n)
           print(pocket_dict[pro])
   ```


## ✅ 후기
1. 

   isalpha : 문자열이 문자인지 아닌지를 True,False로 리턴

   isdigit : 문자열이 숫자인지 아닌지를 True,False로 리턴

   

2. 해당 문자열의 인덱스 찾기

   index : 없으면 에러, 리스트 가능

   find : 없으면 -1, 리스트 안됨



3. index함수는 시간복잡도가 n이고 dictionary는 상수이다.



python 기본함수들은 다시 정리해서 공부해야겠어!