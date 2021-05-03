import sys
input = sys.stdin.readline

n = int(input())
stairs = []
res = []
for i in range(n):
    stairs.append(int(input()))

if n==1:
    print(stairs[0])
    exit()
elif n == 2:
    print(max(stairs[0]+stairs[1], stairs[1]))
    exit()

res.append(stairs[0])
res.append(max(res[0]+stairs[1], stairs[1]))
res.append(max(res[0]+stairs[2], stairs[1]+stairs[2]))

for i in range(3, n):
    res.append(max(res[i-2]+stairs[i], res[i-3]+stairs[i-1]+stairs[i]))

print(res[-1])

