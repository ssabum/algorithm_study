# 1992번 쿼드트리
[문제 보러가기](https://www.acmicpc.net/problem/1992)

## 🅰 코드

```python
# 정답을 담을 변수
result = []
def Test(a):
# 모두 0이거나 모두 1이면 끝
    if sum( sum(a,[]) ) == 0 or len( sum(a,[]) ) == sum(a,[]).count(1):
        if sum( sum(a,[])) == 0:
            result.append('0')
        else:
            result.append('1')
        return
    else:
        result.append('(')
        div = int(len(a)/2) # a/2 x a/2 크기의 행렬을 만들기위해.

        tmp_l =[] # 좌측
        tmp_r =[] # 우측

        #  한행씩 불러온다.
        for sub in a:
            # 1/2 앞쪽 열
            tmp_l.append(sub[0:div])
            # 1/2 뒷쪽 열
            tmp_r.append(sub[div:])

            # tmp_l,tmp_r이 div x div 크기라면
            if len(tmp_l) == div:
                Test(tmp_l) # 좌측값
                Test(tmp_r) # 우측값
                tmp_r = []
                tmp_l = []
        result.append(')')

n = input()
a = []
for i in range(int(n)):
    row = input()
    tmp = []
    for v in row:
        tmp.append(int(v))
    a.append(tmp)
Test(a)

print( ''.join(result) )


```

---


## ✅ 후기
* `분할정복`, `재귀`를 이용한 문제로 큰 가닥을 잡지 못해서 굉장히 헤맸다. 그래서 인터넷의 도움을 사알짝 받긴 했지만... 알고리즘은 다음과 같은 순서로 진행된다.

  ```markdown
  1) 십자가로 쪼갠다.(분할)
  2) 각각의 섹션을 확인한다.
  3) 모두 0이거나 1이라면 출력한다. 아니면 반복한다.
  ```

  ![](README.assets/2.PNG)