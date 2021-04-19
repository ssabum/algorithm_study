# N: 듣도 못한 사람 (~ 500000)
# M: 보도 못한 사람 (~ 500000)
N , M = map(int,input().split())
# 중복되는 이름을 없애기 위해
arr_1 = set()
arr_2 = set()

for _ in range(N):
    arr_1.add(input())
for _ in range(M):
    arr_2.add(input())

# 교집합 개수 출력
arr = sorted(list(arr_1 & arr_2))
print(len(arr))
# 교집합 이름 출력
for i in arr:
    print(i)