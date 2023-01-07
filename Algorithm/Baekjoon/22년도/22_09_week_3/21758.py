N = int(input())
lst = list(map(int, input().split()))
lst_l = lst[:]
lst_r = lst[::-1]

mx = 0
for i in range(1, N):
    lst_r[i] += lst_r[i-1]
    lst_l[i] += lst_l[i-1]

for l in [lst_l, lst_r]:
    for i in range(1, N-1):
        mx = max(mx, 2*l[-1] - l[0] - 2*l[i] + l[i-1])
print(max(mx, sum(lst[1:-1])+max(lst[1:-1])))