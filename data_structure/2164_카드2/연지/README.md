# 2164번 카드2

[문제 보러가기](https://www.acmicpc.net/problem/2164)

🚩 `큐`

<br>

## 🅰 설계

#### 첫 풀이 (fail)

- 1부터 N까지 카드 리스트 만든다음 반복문 돌려서 리스트에 숫자가 1개만 남으면 break 하고 출력
- 한번의 사이클이 돌때마다 맨 앞의 카드 하나 버리고, 그 다음 맨 앞 카드 하나 빼서 맨 뒤에 넣음 -> 즉, `pop(0)` 2번하고 리스트에 append
- 문제 너무 쉽다고 생각했는데 **시간초과** 났다 🙄 ㅋ **범위가 1 ≤ N ≤ 500,000** 이라 그런듯.  ✔ **범위 주의할것**

```python
# 시간초과

N = int(input())
queue = [i for i in range(1, N+1)]  # 1~N 까지 카드 리스트 만들기

while True:  # 일단 계속 돌리다가
    if len(queue) == 1:  # 카드 한장 남으면 반복문 종료
        break

    queue.pop(0)  # 맨 앞 카드 한번 빼주고
    queue.append(queue.pop(0))  # 두번째 카드 (그 다음 맨 앞 카드) 빼서 리스트 맨 뒤에 넣기

print(*queue)
```



#### 두번째 풀이 (fail)

- 그래서 다시 생각해보니, 어차피 맨 앞 숫자 버리고 두번째 숫자만 뒤로 보내면 짝수만 남게됨
- N이 홀수면, `N / 2 4 ... N-1` 이런 순이어서 맨 앞 N은 버리고 2부터 뒤로 보내주면 되고
- N이 짝수면, `2 4 ... N` 이런 순이어서 맨 앞 2는 버리고 4부터 뒤로 보내주면 된다.
- 그래서 이런 풀이를 작성했더니 이번엔 **런타임 에러**가 나왔다 😑

```python
# 런타임 에러 (IndexError)

N = int(input())
queue = [i for i in range(2, N+1, 2)]  # 2부터 짝수만 넣기
if N % 2:  # 홀수면 맨 앞에 N 넣기
    queue.insert(0,N)

while True:
    N = len(queue)
    t = queue[-1]
    if N == 2:
        break
    queue = [queue[i] for i in range(1, N, 2)]
    if N % 2:  # 길이가 홀수면 맨 끝의 숫자 맨 앞에 넣기
        queue.insert(0,t)

print(queue[1])
```



#### 세번째 풀이 (fail)

- 다른 사람들은 어떻게 풀었나 구글링해보니 전부 `deque` 모듈로 풀었다. 그래서 풀었더니 fail ㅋ 😬 

- `queue` 리스트를 만들때 저렇게 만들었더니 **AttributeError** 가 났다.

  > AttributeError 발생 원인
  >
  > - 속성(attribute) 이름이 잘못됐거나 없는 속성을 가져오려고 할 때
  > -  모듈의 함수나 변수를 잘못 입력했을 때 (스펠링, 대소문자)
  > - 식별자(예약어), 내장함수, 모듈 등 이미 존재하는 파이썬 변수명을 사용했을 경우

- 모듈을 불러와서 사용하는데, deque로 처음에 정의를 안해서 그런것 같다.

- 근데 왜 모듈 안쓰고 `pop(0)` 으로 풀었을 때 시간초과가 나는지 모르겠다. 모듈을 불러오고 말고의 차이밖에 없는데 시간이 그렇게 차이 나나 ? -> 아래 후기에 정리해둠

```python
# 런타임 에러 (AttributeError)

from collections import deque

N = int(input())
queue = [i for i in range(1, N+1)]

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())
```

<br><br>

## 🅱 최종 코드

핵심 포인트는 `deque` 라이브러리를 사용하는 것

처음 큐를 정의할 때 `deque()` 도 잊지말자

```python
from collections import deque

N = int(input())
queue = deque()

for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())
```

<br><br>

## ✅ 후기

### 새롭게 알게 된 점

- `deque` 모듈  [deque 파이썬 공식문서](https://docs.python.org/ko/3/library/collections.html#collections.deque)

- `AttributeError` 발생 원인

- 큐랑 deque랑 여태 같은 건줄 ;; 근데 블로그 글 봐도 잘 모르겠다.. 어차피 전부 시간복잡도 O(1)인데 도대체 뭔 차이일까,,,  [스택, 큐, 덱(deque) 차이점](https://velog.io/@choiiis/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue) , [Python 컨테이너 메소드의 시간복잡도](https://daimhada.tistory.com/56)

- ⭐  출처 :  [파이썬 deque 사용하는 이유](https://scribblinganything.tistory.com/31)

  대박. **파이썬 deque를 사용하는 이유를 찾았다. 차이는 `popleft`의 시간차이다 !!!!!**

  list의 경우 pop()으로 마지막 값을 꺼내는 경우 O(1) (일정한 시간) 시간이 걸리는데, pop(0)으로 가장 앞단에 값을 꺼낼때는 list 크기에 따라 읽어 오는 시간이 달라진다. O(n) 시간이 걸린다.

  하지만 deque를 사용할 경우 popleft()를 사용하면 리스트의 pop(0)과 같은 기능을 주면서 걸리는 시간은 O(1)이 걸린다.

### 어려웠던 점

- 시간초과, 런타임에러로 한참을 고민했다. 분명 코드는 맞는데 계속 에러가 나니까 작업 과정을 줄여야될거 같아서 그렇게 코드를 짰더니 또 시간초과가 나와서 답답했다.
- 정답을 알고 난 뒤의 허탈감이란.... ㅋ
- 문제는 분명 쉬웠는데 `deque` 모듈로 풀어야한다는걸 한번에 캐치하지 못했다.



