T = int(input())

for t in range(1, T+1):
    day = int(input())
    price = list(map(int, input().split()))
    m_p = price[-1]
    bnf = 0
    for i in range(day-2, -1, -1):
        if price[i] < m_p:
            bnf += m_p - price[i]
        elif price[i] > m_p:
            m_p = price[i]

    print(f'#{t} {bnf}')

