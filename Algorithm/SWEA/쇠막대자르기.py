T = int(input())
for t in range(1, T+1):
    P = input()
    p_l = None
    cut = ps = t_ps = 0
       
    for p in P:
        if p == '(':
            p_l = '('
            t_ps += 1
            ps += 1
        else:
            ps -= 1
            if p_l == '(':
                t_ps -= 1
                p_l = None
                cut += ps
        
    print(f'#{t} {t_ps + cut}')