import sys
sys.stdin = open("input.txt")


input_lst = input().split('-')

tmp = input_lst[0].split('+')
res = 0
for ele in tmp:
    res += int(ele)

for i in range(1, len(input_lst)):
    tmp = input_lst[i].split('+')
    for ele in tmp:
        res -= int(ele)

print(res)

