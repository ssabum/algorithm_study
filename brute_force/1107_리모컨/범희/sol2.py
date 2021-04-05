import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
li = set(list(sys.stdin.readline().split()))
res = abs(100-n)
for i in range(1000000):
    ba = set(list(str(i)))
    le = len(str(i))
    if not ba&li:
        res = min(res,le+abs(n-i))
print(res)
