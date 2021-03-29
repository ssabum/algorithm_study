# N, r, c = map(int, input().split()) # 2^N 한 변의 길이


def order(N, r, c):
    if N == 0:
        return 0
    if r < 2**(N-1) and c < 2**(N-1):
        return order(N-1, r, c)
    elif r < 2**(N-1) and c >= 2**(N-1):
        return 2**(2*N-2) + order(N-1, r, c-2**(N-1))
    elif r >= 2**(N-1) and c < 2**(N-1):
        return 2*2**(2*N-2) + order(N-1, r-2**(N-1), c)
    elif r >= 2**(N-1) and c >= 2**(N-1):
        return 3*2**(2*N-2) + order(N-1, r-2**(N-1), c-2**(N-1))

for r in range(16):
    for c in range(16):
        print(order(4, r, c), end=" ")
    print()
