n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# 람다함수 쓰는것 익숙해지기!!!
arr.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0
for i in range(n):
    if end <= arr[i][0]:
        count += 1
        end = arr[i][1]

print(count)