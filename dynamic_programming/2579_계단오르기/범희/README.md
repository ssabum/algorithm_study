# 2579번 계단 오르기
[문제 보러가기](https://www.acmicpc.net/problem/2579)

## 🅰 코드

```python
import sys
input = sys.stdin.readline

n = int(input())
stairs = []
res = []
for i in range(n):
    stairs.append(int(input()))

if n==1:
    print(stairs[0])
    exit()
elif n == 2:
    print(max(stairs[0]+stairs[1], stairs[1]))
    exit()

res.append(stairs[0])
res.append(max(res[0]+stairs[1], stairs[1]))
res.append(max(res[0]+stairs[2], stairs[1]+stairs[2]))

for i in range(3, n):
    res.append(max(res[i-2]+stairs[i], res[i-3]+stairs[i-1]+stairs[i]))

print(res[-1])

```

---


## ✅ 후기
* `DP`문제로 각 계단의 경우의 수마다 2가지의 경우를 고려하면서 진행해 나간다.

  ```markdown
  첫번째 경우) 2계단 전에서 한번에 올라오는 경우
  두번째 경우) 3계단 전에서 2계단 한번에 올라온 후 1계단 올라온 경우
  ```

  