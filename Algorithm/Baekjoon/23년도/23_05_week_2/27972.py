N = int(input())
lst = list(map(int, input().split()))

mx = 0
now_num = 0
pre_num = lst[0]
flag = False
for n in lst:
    if n > pre_num:
        if flag:
            now_num += 1
        else:
            flag = True
            now_num = 1

    elif n < pre_num:
        if flag:
            flag = False
            now_num = 1
        else:
            now_num += 1

    mx = max(mx, now_num)

    pre_num = n

print(mx + 1)
