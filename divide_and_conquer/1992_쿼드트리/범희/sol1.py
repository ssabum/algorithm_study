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

