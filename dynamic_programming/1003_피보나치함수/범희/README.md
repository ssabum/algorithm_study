# 1003번_피보나치 함수
[문제 보러가기](https://www.acmicpc.net/problem/1003)

## 🅰 설계

```python
t = int(input())
for i in range(t):
    n = int(input())
    # fib(0), fib(1), tmp 설정
    zero, one, tmp = 1, 0, 0
    # 피보나치 수행
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    # 출력
    print(zero, one)
```

---


## ✅ 후기
// 풀이과정

* 처음 문제를 읽고 어떻게 해야할지 풀이가 떠오르지 않아 꽤나 고생했다.😥
* 하지만 `5`까지의 경우의 수를 직접 표로 그려보니 간단한 문제임을 알 수 있었다.
* `fib(0)`, `fib(1)`의 카운트를 담을 변수를 생성하고 `n`이 커질수록 증가하는 규칙을 찾아서 코드로 옮겨주기만 하면 되는 문제였다.👍

// 앞으로 다짐

* 문제 풀이가 떠오르지 않을 땐 무조건 노트에 그려보자!!!