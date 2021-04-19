N, M = map(int, input().split())

set_N = set()
set_M = set()
for _ in range(N):
    set_N.add(input())
for _ in range(M):
    set_M.add(input())

res = sorted(list(set_N & set_M))

print(len(res))
for ele in res:
    print(ele)