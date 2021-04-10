N, M = map(int, input().split())
# 1부터 N까지의 자연수 중에 중복없이 M개 고른 수열

sel = []
i = 1

def perm(n, m):
    if len(sel) == m:
        print(*sel)
    
    for i in range(1, n+1):
        if i not in sel:
            sel.append(i)
            perm(n, m)
            sel.pop()

# perm(3, 2)
perm(M, N)