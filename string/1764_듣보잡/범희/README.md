# 1764번 듣보잡
[문제 보러가기](https://www.acmicpc.net/problem/1764)

## 🅰 코드

```python
# N: 듣도 못한 사람 (~ 500000)
# M: 보도 못한 사람 (~ 500000)
N , M = map(int,input().split())
# 중복되는 이름을 없애기 위해
arr_N = set()
arr_M = set()

for _ in range(N):
    arr_N.add(input())
for _ in range(M):
    arr_M.add(input())

# 교집합 개수 출력
arr = sorted(list(arr_N & arr_M))
print(len(arr))
# 교집합 이름 출력
for i in arr:
    print(i)
    
```

---


## ✅ 후기
* 문제에서 주어진 대로 중복을 허용하지 않는 두개의 그룹`SET`으로 나누어 차례로 추가해주고 출력해주는 문제였다.

* 문제 진행에 있어 교집합을 구하는 부분이 등장하는데 이때 교집합 뿐만 아니라 합집합, 차집합 등 다양한 집합을 `python`으로 다루는 내용을 정리한 [페이지](https://pydole.tistory.com/entry/Python-%EA%B5%90%EC%A7%91%ED%95%A9-%ED%95%A9%EC%A7%91%ED%95%A9-%EC%B0%A8%EC%A7%91%ED%95%A9)를 참조했다.

  > 참고로 `대칭차집합`은 합집합에서 교집합을 뺀 집합을 지칭한다.