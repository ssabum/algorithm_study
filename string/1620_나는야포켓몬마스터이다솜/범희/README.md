# 1620번 나는야 포켓몬 마스터 이다솜
[문제 보러가기](https://www.acmicpc.net/problem/1620)

## 🅰 코드

```python
# 데이터 입력
N, M = map(int,input().split())
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
```

---


## ✅ 후기
* 일단 문제를 읽기 싫었다...`포켓몬`컨셉인건 알겠는데 사설이 너무 길다... 나중에 기회가 된다면 내가 직접 `깔끔하고 섹시한` 문제를 만들어 올릴 것이다.
* 문제에 대한 접근은 `리스트`, `딕셔너리` 형태로 문제에서 주어진 데이터들을 저장한 후 검색해 출력하는 문제이다.
* 예전에 `python` 처음 배울때 알아 두었던 [내장함수](https://docs.python.org/ko/3/library/functions.html) 덕에 쉽게 접근 할 수 있었다. 역시 기본이 튼튼해야 문제를 쉽게 해결 할 수 있다.😮
