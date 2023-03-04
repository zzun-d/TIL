
r1, c1, r2, c2 = map(int, input().split())
mx = max(2*max(r1,c1,r2,c2), -2*min(r1,c1,r2,c2))
arr = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]

i = j = 0
n = 1
total = (r2-r1+1) * (c2-c1+1) 
if r2 >= i >= r1 and c2 >= j >=c1:
    arr[i-r1][j-c1] = str(n)
    m = '1'
    total -= 1
cnt = 1
d = 0
tmp = False
direct = [[0, 1], [-1, 0], [0, -1], [1, 0]]
while total > 0:
    for _ in range(cnt):
        n += 1
        i += direct[d][0]
        j += direct[d][1]
        if r2 >= i >= r1 and c2 >= j >=c1:
            arr[i-r1][j-c1] = str(n)
            m = str(n)
            total -= 1
    d = (d+1) % 4
    if tmp:
        cnt += 1
        tmp=False
    else:
        tmp=True


nm = (mx + 1)**2
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(arr[i][j]).rjust(len(m)), end=" ")
    print()