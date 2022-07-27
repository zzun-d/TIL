t = int(input())

for i in range(t):
    input()
    c_m, y, s_su, s_sa, f = map(int, input().split())
    b, g_s, g_c, w = map(int, input().split())
    banjook = int(min(c_m/8, y/8, s_su/4, s_sa, f/9) * 16)
    able_cake_num = b + g_s//30 + g_c//25 + w//10
    if banjook >= able_cake_num:
        print(able_cake_num)
    else:
        print(banjook)