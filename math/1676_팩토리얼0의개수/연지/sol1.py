N = int(input())
t = N - N % 5
ans = 0
while t >= 5:
    ans += t // 5
    t //= 5

print(ans)