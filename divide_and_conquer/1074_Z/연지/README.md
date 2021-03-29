# 1074번 Z

[문제 보러가기](https://www.acmicpc.net/problem/1074)

🚩 `분할정복`, `재귀`

<br>

## 🅰 설계

1. 처음 풀이 (fail)

아웃풋이 15, 63으로 나왔다. 원래(11, 63)이 맞음. 

디버깅해보니 📍 부분에서 함수가 종료되어야하는데 다음 divide함수 (`divide(s_x + N // 2, s_y + N // 2, N // 2)`) 호출이 되서 함수가 종료되지 못했다.

```python
def divide(s_x, s_y, N):
    global cnt
    if N == 2:
        if s_x == r and s_y == c:  # 1위치
            return
        if s_x == r and s_y+1 == c:  # 2위치
            cnt += 1
            return
        if s_x+1 == r and s_y == c:  # 3위치
            cnt += 2
            return
        if s_x+1 == r and s_y+1 == c:  # 4위치
            cnt += 3
            return # 📍
        else:
            cnt += 4
            return
    else:
        divide(s_x, s_y, N // 2)
        divide(s_x, s_y + N // 2, N // 2)
        divide(s_x + N // 2, s_y, N // 2)
        divide(s_x + N // 2, s_y + N // 2, N // 2)


T = int(input())
for tc in range(1, T+1):
    N, r, c = map(int, input().split())

    cnt = 0
    divide(0,0,2**N)

    print(cnt)
```

2. 시간초과 (fail)

함수 내에서 바로 프린트 후 return 하도록 바꿨더니 `(r,c)`일때 함수가 잘 종료되고 output도 맞게 나왔는데 시간초과 뜸

```python
def divide(s_x, s_y, N):
    global cnt
    if N == 2:
        if s_x == r and s_y == c:  # 1위치
            print(cnt)
            return
        if s_x == r and s_y+1 == c:  # 2위치
            cnt += 1
            print(cnt)
            return
        if s_x+1 == r and s_y == c:  # 3위치
            cnt += 2
            print(cnt)
            return
        if s_x+1 == r and s_y+1 == c:  # 4위치
            cnt += 3
            print(cnt)
            return
        else:
            cnt += 4
            return
    else:
        divide(s_x, s_y, N // 2)
        divide(s_x, s_y + N // 2, N // 2)
        divide(s_x + N // 2, s_y, N // 2)
        divide(s_x + N // 2, s_y + N // 2, N // 2)


N, r, c = map(int, input().split())

cnt = 0
divide(0,0,2**N)
```

3. success

마지막 else문의 범위를 나눴더니 맞았다. 뭔가 알고리즘 문제라기보다 수학문제 같았던.. 노가다의 향연이었다

<br><br>

## 🅱 최종 코드

```python
def divide(s_x, s_y, N):
    global cnt
    if N == 2:
        if s_x == r and s_y == c:  # 1위치
            print(cnt)
            return
        if s_x == r and s_y+1 == c:  # 2위치
            cnt += 1
            print(cnt)
            return
        if s_x+1 == r and s_y == c:  # 3위치
            cnt += 2
            print(cnt)
            return
        if s_x+1 == r and s_y+1 == c:  # 4위치
            cnt += 3
            print(cnt)
            return
        else:
            cnt += 4
            return
    else:
        half = N // 2
        if s_x <= r < s_x + half and s_y <= c < s_y + half:  # 1사분면
            divide(s_x, s_y, half)
        elif s_x <= r < s_x + half and s_y + half <= c < s_y + 2*half:  # 2사분면
            cnt += half*half
            divide(s_x, s_y + half, half)
        elif s_x + half <= r < s_x + 2*half and s_y <= c < s_y + half:  # 3사분면
            cnt += half*half*2
            divide(s_x + half, s_y, half)
        elif s_x + half <= r < s_x + 2*half and s_y + half <= c < s_y + 2*half:  # 4사분면
            cnt += half*half*3
            divide(s_x + half, s_y + half, half)


N, r, c = map(int, input().split())

cnt = 0
divide(0,0,2**N)
```

<br><br>

## ✅ 후기

알고리즘 맨날맨날 풀어야겠다. 제곱 어케 쓰는지도 까먹음 환장  `2**N`

[2630 색종이 만들기](https://github.com/ssabum/algorithm_study/tree/master/divide_and_conquer/2630_%EC%83%89%EC%A2%85%EC%9D%B4%20%EB%A7%8C%EB%93%A4%EA%B8%B0)랑 풀이가 비슷했지만 (재귀적으로 절반으로 나눠서 해결하는 문제) 범위체킹때문에 더 복잡했다.

swea보다 백준이 더 까다로운거 같다.

### 어려웠던 점

everyday 시~ 간~ 초~ 과~ 🤮