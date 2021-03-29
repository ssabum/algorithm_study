# 1074번_Z
[문제 보러가기](https://www.acmicpc.net/problem/1074)

## 🅰 설계

```python
import sys
result = 0

def z(n, x, y):
    global result
    # 기본이 되는 탈출 조건 생성
    if x == r and y == c:
        print(int(result))
        exit(0)
    if n == 1:
        result += 1
        return
    # 처음에 시간초과 떠서 경우의 수도 합쳐 주었다.
    # 하지만 나중에 알고보니 할 필요 없었다...
    if not (x <= r < x + n and y <= c < y + n):
        result += n * n
        return
    # 재귀함수
    z(n / 2, x, y)
    z(n / 2, x, y + n / 2)
    z(n / 2, x + n / 2, y)
    z(n / 2, x + n / 2, y + n / 2)

# 시간초과 안나기 위해 sys.stdin.readline사용...sibal...
n, r, c = map(int, sys.stdin.readline().split(' '))
z(2 ** n, 0, 0)
```

---


## ✅ 후기
// 풀이과정

* 문제에 주어진 그림을 보면서 이해를 쉽게 할 수 있었다.

* 다만 요건은 `시간초과`였다.

  시간초과를 없애기 위해 `if`문을 합쳐 보면서 어떻게든 줄여보려 했지만 결과는 `시관초과`...

* 이후 검색을 통해 `sys.stdin.readline()`에 대해 알게 되었고 이를 이용해 해결 할 수 있었다.

  [sys.stdin.readline사용법](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
