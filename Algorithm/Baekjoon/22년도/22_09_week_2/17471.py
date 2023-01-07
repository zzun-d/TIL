from collections import defaultdict

def groups(n, lst_a):     # 구역 나누는 함수
    if n > N:           # 종료 조건(구역 수 보다 커지면)
        div_lst = []
        lst_b = []
        for i in range(1, N+1):     # a구역: lst_a, b구역: lst_b
            if i not in lst_a:
                lst_b.append(i)
        div_lst.append(lst_a[:])
        div_lst.append(lst_b[:])
        pos_lst.append(div_lst[:])  # possible 리스트에 a구역, b구역 나눠진 리스트 append
        return

    lst_a.append(n)
    groups(n+1, lst_a)
    lst_a.pop()
    groups(n+1, lst_a)

N = int(input())
people = [0] + list(map(int, input().split()))
graph = defaultdict(list)

for i in range(1, N+1):             # graph dict 형태로 나타냄(key는 구역, value는 연결된 구역들)
    info = list(map(int, input().split()))
    for j in range(1, info[0]+1):
        graph[i].append(info[j])
pos_lst = []
groups(1, [])

result = 10000                      # 인구 수 차이 초기값 설정

for a, b in pos_lst:                # 경우의 수 탐색(a구역, b구역)
    if 0 < len(a) < N:              # 공집합, 자기자신 제외
        cnt_a = 0
        cnt_b = 0
        a_set = set(a)
        b_set = set(b)
        if len(a) != 1:             # a구역이 하나면 연결 여부 확인 불필요, 1이 아닐때만 확인
            V = [a[0]]              # a구역의 첫 구역을 시작으로 모두 연결되어 있는지 집합을 이용하여 확인
            while V:
                nv = []
                for v in V:
                    nv += [i for i in graph[v] if i in a_set]
                a_set -= set(nv)        
                V = nv
            if a_set:               # 방문 못한 a구역이 존재하면 다음 경우의 수로 ㄱㄱ
                continue

        if len(b) != 1:             # b도 마찬가지
            V = [b[0]]
            while V:
                nv = []
                for v in V:
                    nv += [i for i in graph[v] if i in b_set]
                b_set -= set(nv)
                V = nv
            if b_set:
                continue

        for n in a:                 # a구역, b구역 인구수 계산
            cnt_a += people[n]
        for n in b:
            cnt_b += people[n]

        result = min(result, abs(cnt_a - cnt_b))        # 결과 갱신


if result == 10000:         # 결과가 바뀌지 않았으면 가능한 경우의 수 존재하지 않음 => -1 출력
    print(-1)
else:    
    print(result)