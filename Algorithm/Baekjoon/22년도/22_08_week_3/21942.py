import sys

def input():
    return sys.stdin.readline().rstrip()
m_d = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]    # 월별 날짜 계산용

def durate(D1, D2, T1, T2):                     # 기간을 분으로 환산 해주는 함수
    _, M1, d1 = list(map(int, D1.split('-')))
    _, M2, d2 = list(map(int, D2.split('-')))
    day = m_d[M2] - m_d[M1] + d2 - d1
    h1, m1 = list(map(int, T1.split(':')))
    h2, m2 = list(map(int, T2.split(':')))
    return (h2 - h1) * 60 + (m2 - m1) + day * 1440

N, L, F = input().split()

N, F = int(N), int(F)
d, h_m = L.split('/')
h, m = map(int, h_m.split(':'))
L = int(d) * 1440 + h * 60 + m
b_note = {}
for _ in range(N):                                  # b_note dict에 key를 빌린사람 이름, value를 빌린 목록
    D, T, product, name = list(input().split())
    if b_note.get(name):
        if b_note[name].get(product):               # 빌린 목록이 있는데 해당 물건 다시 들어오면 반납, 기간 확인 및 벌금 적립
            dur = durate(b_note[name][product].pop(), D, b_note[name][product].pop(), T)
            if dur > L:
                if b_note[name].get('pay_'):
                    b_note[name]['pay_'] += (dur-L) * F
                else:
                    b_note[name]['pay_'] = (dur-L) * F
        else:
            b_note[name][product] = [T, D]
    else:
        b_note[name] = {product:[T, D]}

k_lst = list(b_note.keys())
k_lst.sort()                # 사전순으로 이름 정렬
ans = []
for k in k_lst:             # 지불할 벌금이 있으면 ans에 이름, 벌금 append
    if b_note[k].get('pay_'):
        ans.append(k)
        ans.append(b_note[k]['pay_'])
if ans:                     # 이름, 벌금 print
    for i in range(0, len(ans), 2):
        print(ans[i], ans[i+1])
else:                       # 벌금 낼 사람 없으면 -1 print
    print(-1)
