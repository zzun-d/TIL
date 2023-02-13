
working = 0
for _ in range(5):
    s, e = input().split()
    s_h, s_m = map(int, s.split(':'))
    e_h, e_m = map(int, e.split(':'))
    working += (e_h - s_h)*60 + (e_m - s_m)
print(working)