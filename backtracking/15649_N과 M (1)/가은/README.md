# 15649_N과 M(1)
[문제 보러가기]()

## 🅰 설계

```python
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
```

이전에는

 visited를 사용해서 해당 sel에 원소가 들어있는지 아닌지를 체크하는데 

이번에는

`in` 으로 간단하게 방문(들어있는지) 체크

## ✅ 후기

재업!

재귀문제 너무 어렵고 다시 풀었는데도 결국 스스로 풀지 못하고 답을 봤다.ㅠㅜ

