# 1780번 종이의 개수

[문제 보러가기](https://www.acmicpc.net/problem/1780)

🚩 `분할정복`, `재귀`

<br>

## 🅰 설계

N이 3의 배수이기 때문에 같은 숫자로 안 이루어져 있으면 계속해서 나누면서 `-1, 0, 1` 의 개수를 구하면 된다.

그래서 같은 숫자로 이루어져 있는지 체크하는 `checking` 이라는 함수와 9칸으로 행렬을 나눌 `divide` 라는 함수를 만들어 구했다.

시작행(`s_x`)과 시작열 (`s_y`) 을 인자로 하여 함수를 계속 쪼개더라도 값을 확인할 수 있도록 구성했다.

처음 코드를 짤 때 1️⃣과 2️⃣의 순서를 바꿨더니 틀렸다. 일단 어떤 값이 나왔는지를 먼저 체크해야하기 때문에 1️⃣과 2️⃣의 순서로 구성해야한다.

<br>

## 🅱 최종 코드

```python
# 같은 숫자로 이루어져 있는지 확인하는 함수
def checking(s_x, s_y, length):  # 시작 x, y좌표, 종이 길이
    global res
    check = []  # 숫자값을 넣을 리스트
    for i in range(s_x, s_x+length):
        for j in range(s_y, s_y+length):
            if a[i][j] not in check:  # 1️⃣ check에 값이 없으면 넣어주기
                check.append(a[i][j])
            if len(check) >= 2:  # 2️⃣ 개수가 두개 이상 나온 경우 함수 쪼개야 하므로 쪼개고 리턴
                divide(s_x, s_y, length)
                return
    # 같은 종이로 이루어진 경우
    if check[0] == -1:
        res[0] += 1
    elif check[0] == 0:
        res[1] += 1
    elif check[0] == 1:
        res[2] += 1


# 3으로 나누는(== 9칸으로 나누는) 함수
def divide(s_x, s_y, length):
    global res
    if length == 1:
        res[a[s_x][s_y]] += 1
        return  # 더이상 나누지 않음
    k = length//3
    checking(s_x, s_y, k)
    checking(s_x, s_y+k, k)
    checking(s_x, s_y+2*k, k)
    checking(s_x+k, s_y, k)
    checking(s_x+k, s_y+k, k)
    checking(s_x+k, s_y+2*k, k)
    checking(s_x+2*k, s_y, k)
    checking(s_x+2*k, s_y+k, k)
    checking(s_x+2*k, s_y+2*k, k)



N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
res = [0, 0, 0]  # -1개수, 0개수, 1개수
checking(0, 0, N)

print(res[0])
print(res[1])
print(res[2])
```

<br>

## ✅ 후기

코드 참 그지같다... 너무 길고 느리고..

답은 맞았으나 나의 알고리즘 실력은 그대로 인것 같아 기분이 구리다

언제쯤 코드를 기깔나게 효율적이고 간결하게 짤 수 있을까

메모리랑 시간 진심 머선129 . . .

![1780_memory time](https://user-images.githubusercontent.com/77573938/116852623-9fd66380-ac2f-11eb-93ca-429ada44fb2e.png)