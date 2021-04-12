# 데이터 입력
N , M = map(int,input().split())
# 포켓몬을 '이름:번호'로 딕셔너리 생성
arr = [0]
dict = {}
for num in range(1,N+1):
    monster = input().strip()
    arr.append(monster)
    dict[monster] = num
# 주어진 문제에 대해 숫자인지, 문자인지 판별 후 검색
for _ in range(M):
    q = input().strip()
    if q.isalpha() :
        print(dict[q])
    elif q.isdigit() :
        print(arr[int(q)])