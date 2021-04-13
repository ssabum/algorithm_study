import sys
sys.stdin = open('input.txt')
'''
isalpha : 문자열이 문자인지 아닌지를 True,False로 리턴
isdigit : 문자열이 숫자인지 아닌지를 True,False로 리턴

* 해당 문자열의 인덱스 찾기
index : 없으면 에러, 리스트 가능
find : 없으면 -1, 리스트 안됨
'''

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

'''
시간초과때문에 dictionary로 풀어야됨
dictionary 가 hash임 해당 값을 찾는데에 O(1)
'''