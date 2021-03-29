import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    N = int(input())
    # 0의 개수
    count0 = 0
    # 1의 개수
    count1 = 0


    def fibo(n):
        global count0, count1
        if n == 0:
            count0 += 1
            return 0
        elif n == 1:
            count1 += 1
            return 1
        return fibo(n - 1) + fibo(n - 2)


# 시간 초과
# 피보나치 계산을 전부할 필요가 없나?
# memoization?
    c = [[0, 0]] * (N+1)
    def fibo1(n):
        global c
        if n == 0:
            c[0] = [1, 0]
            return c[0]
        elif n == 1:
            c[1] = [0, 1]
            return c[1]
        a1, a2 = fibo1(n-1)
        a3, a4 = fibo1(n-2)
        c[n] = [a1+a3, a2+a4]
        return c[n]

    # print(*fibo1(N))

# memoization 잘못했네
    c = [[0, 0]] * (N + 1)
    def fibo2(n):
        global c
        if n == 0:
            c[0] = [1, 0]
            return c[0]
        elif n == 1:
            c[1] = [0, 1]
            return c[1]
        elif c[n] != [0, 0]:
            return c[n]
        else:
            a1, a2 = fibo2(n - 1)
            a3, a4 = fibo2(n - 2)
            c[n] = [a1 + a3, a2 + a4]
            return c[n]

    print(*fibo2(N))

