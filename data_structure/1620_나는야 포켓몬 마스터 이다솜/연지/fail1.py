import sys
sys.stdin = open("input.txt")


N, M = map(int, input().split())
lst = [input() for _ in range(N)]
quest = [input() for _ in range(M)]
for j in range(M):
    for i, v in enumerate(lst):
    # print(i, type(i), v, type(v))  # 0 <class 'int'> Bulbasaur <class 'str'>
        if quest[j] == v:
            print(i+1)
        if quest[j] == str(i+1):
            print(v)


