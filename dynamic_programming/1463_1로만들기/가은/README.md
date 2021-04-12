# 1463번 1로 만들기
[문제 보러가기](https://www.acmicpc.net/problem/1463)

## 🅰 설계

1. 단순하게 n/3, n/2, n-1순서대로 함수를 짰다.

   ```python
   def cal(n):
       global cnt
       if n == 1:
           return
       cnt[0] +=1
       if not n % 3:
           cal(n // 3)
       elif not n % 2:
           cal(n // 2)
       else:
           cal(n - 1)
   ```

2. 10이 예외로 발생해서 3으로 나눴을 때 1이 남는 수에 대해서 처리해주는 함수를 만들었다.

   또, 앞에 만든 함수에서의 결과와의 최솟값을 구했다.

   ```python
   cnt = [0, 0, 0]
   
   def cal2(n):
       if n == 1:
           return
       global cnt
       cnt[1] +=1
       if not n % 3:
           cal2(n // 3)
       elif n % 3 == 1:
           cnt[1] += 1
           cal2((n - 1)//3)
       elif not n % 2:
           cal2(n // 2)
       else:
           cal2(n - 1)
          
   min(cnt)
   ```



:exclamation: 틀린 이유: 항상 예외가 존재한다. 숫자가 1로 가는 과정에서 늘 같은 알고리즘(예: 3으로 나눈다. 2로 나눈다. 1을 뺀다.) 으로 계산을 하는 게 아니라 과정에서 최소연산횟수가 되는 알고리즘이 필요한 것같다.



3. 정답코드

DP로 풀어야 한다.. :sweat:

점화식 : dp(N) = min ( dp(N//3) +1, dp(N//2)+1 , dp(N-1)+1 )

매번 3개의 방법을 써서 최소연산횟수를 구한다.

```python
n = int(input())

# i번 째 인덱스가 i가 1이 되는 최소연산횟수
dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    # 1을 뺐을 때 연산 횟수
    dp[i] = dp[i-1] + 1  

    # 2로 연산했을 때보다 현재 존재하는 연산횟수가 더 클 때
    if i%2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2]+1
        
    # 3으로 연산했을 때보다 현재 존재하는 연산횟수가 더 클 때
    if i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1

print(dp[n])
```

다시 풀어보자... 구글링해서도 겨우 코드만 이해함


## ✅ 후기
매 과정마다 다른 연산을 써야하는 경우, 다른 알고리즘을 써야하는 경우는 dp를 고려해보자