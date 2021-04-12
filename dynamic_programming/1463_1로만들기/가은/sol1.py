'''
점화식 : dp(N) = min ( dp(N//3) +1, dp(N//2)+1 , dp(N-1)+1 )
'''
# n = int(input())
n = 10

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

print(dp)
print(dp[n])