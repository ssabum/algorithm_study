# '-'부호로 나눠진 문자열 저장
arr = input().split('-')
# 결과 변수 생성
result = 0
# 처음 '-'부호가 나오는 부분까지 더하기
for i in arr[0].split('+'):
    result += int(i)
# 그 뒤엔 다 빼주는데 '+'부호로 묶인 것도 나눠서 빼기 → -(a+b) = -a-b
for i in arr[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)