# 1927번 최소힙
[문제 보러가기](https://www.acmicpc.net/problem/1927)

## 🅰 코드

```python
import heapq
import sys

N = int(input())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
        
```

---


## ✅ 후기
* `heap`을 다루는 문제로 숫자가 들어왔을 때는 `heappush`로 출력하고 `0`이 들어오면 `heappop`을 한 뒤 `print`를 하도록 구상하였다.

* 이 문제의 중점은 시간단축을 위해 `sys.stdin.readline()`과 `heapq`을 사용하는 것이다. 전에도 종종 언급했었지만 다시한번 정리하자면 인풋받는 메소드의 속도차이는 다음과 같다.

  ```python
  sys.stdin.readline < raw_input() < input()
  # sys.sydin.readline: 한줄의 문자열을 통째로 반환 / sys.stdin: 여러줄 입력받을 때
  # raw_line: 문자열을 반환
  # input: raw_input을 evaluate한 결과를 반환
  ```