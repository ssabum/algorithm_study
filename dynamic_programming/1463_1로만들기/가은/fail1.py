# N = int(input())

'''
정수 N을 1로 만들기
최소연산횟수
'''
cnt = [0, 0, 0]
def cal(n):
    global cnt
    if n == 1:
        return
    cnt[0] +=1
    if not n % 3:
        cal(n // 3)
    elif not n % 2:
        cal(n // 2)
    else:
        cal(n - 1)

def cal2(n):
    if n == 1:
        return
    global cnt
    cnt[1] +=1
    if not n % 3:
        cal2(n // 3)
    elif n % 3 == 1:
        cnt[1] += 1
        cal2((n - 1)//3)
    elif not n % 2:
        cal2(n // 2)
    else:
        cal2(n - 1)

def cal3(n):
    if n == 1:
        return
    global cnt
    cnt[2] +=1
    if not n % 3:
        cal3(n // 3)
    elif n % 3 == 1:
        cnt[2] += 1
        cal3((n - 1)//3)
    elif n % 3 == 2:
        cnt[2] += 2
        cal3((n - 2)//3)
    elif not n % 2:
        cal3(n // 2)
    else:
        cal3(n - 1)

N = 17
cal(N)
cal2(N)
cal3(N)
print(cnt)