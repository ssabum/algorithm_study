import sys
sys.stdin = open("input.txt")

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
